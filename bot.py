import os
import json
import time
import threading
import asyncio
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import discord
from discord.ext import commands

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# === Discord Setup ===
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

already_sent = set()

class LinkButtonView(discord.ui.View):
    def __init__(self, link):
        super().__init__()
        self.add_item(discord.ui.Button(label="🔗 Zum Angebot", style=discord.ButtonStyle.link, url=link))

async def send_new_items():
    await bot.wait_until_ready()
    channel = bot.get_channel(1388957925531451479)
    
    global already_sent

    while not bot.is_closed():
        try:
            with open('data.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            for item in data:
                link = item.get("link")
                if link not in already_sent:
                    already_sent.add(link)

                    embed = discord.Embed(
                        title=f"🛍️ {item['name']}",
                        color=discord.Color.green()
                    )

                    img = item.get("image", "")
                    if img.startswith("http"):
                        embed.set_image(url=img)

                    embed.add_field(name="💰 Preis", value=item.get('price', 'Keine Angabe'), inline=False)
                    embed.add_field(name="📏 Größe", value=item.get('size', 'Keine Angabe'), inline=False)
                    embed.add_field(name="🏷️ Marke", value=item.get('brand', 'Keine Angabe'), inline=False)
                    embed.add_field(name="✨ Zustand", value=item.get('condition', 'Keine Angabe'), inline=False)

                    await channel.send(embed=embed, view=LinkButtonView(link))
                    await asyncio.sleep(2)

        except Exception as e:
            print(f"Fehler beim Senden: {e}")
        
        await asyncio.sleep(60)

@bot.event
async def on_ready():
    print(f"Bot ist eingeloggt als {bot.user}")
    bot.loop.create_task(send_new_items())

# === Scraper in separatem Thread ===
def run_scraper():
    options = Options()
    options.add_experimental_option(name='detach', value=True)
    options.add_argument("user-agent=Mozilla/5.0 ... Chrome/124.0.0.0 Safari/537.36")

    # WebDriverManager verwenden
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    seen_links = set()

    if os.path.exists("data.json"):
        with open("data.json", "r", encoding="utf-8") as f:
            try:
                old_data = json.load(f)
                seen_links = {item["link"] for item in old_data}
            except:
                pass

    results = list(seen_links)

    website = 'https://www.vinted.de/catalog?search_text=Nike%20Hose'

    while True:
        try:
            driver.get(website)
            time.sleep(5)

            try:
                accept = driver.find_element(By.ID, "onetrust-reject-all-handler")
                accept.click()
            except:
                pass

            items = driver.find_elements(By.XPATH, "//div[contains(@class, 'feed-grid')]")

            new_results = []
            for item in items:
                try:
                    link_elem = item.find_element(By.XPATH, ".//a[contains(@class, 'new-item-box__overlay--clickable')]")
                    link = link_elem.get_attribute("href")
                    if link in seen_links:
                        continue
                    seen_links.add(link)

                    title = link_elem.get_attribute("title")
                    name = title.split(",")[0].strip()

                    try:
                        price = item.find_element(By.XPATH, ".//span[contains(text(), '€')]").text.strip()
                    except:
                        price = "N/A"

                    try:
                        img = item.find_element(By.XPATH, ".//img").get_attribute("src")
                    except:
                        img = "N/A"

                    try:
                        brand = item.find_element(By.XPATH, ".//p[contains(@data-testid, '--description-title')]").text.strip()
                    except:
                        brand = "N/A"

                    try:
                        subtitle = item.find_element(By.XPATH, ".//p[contains(@data-testid, '--description-subtitle')]").text.strip()
                        parts = subtitle.split("·")
                        size = parts[0].strip() if len(parts) > 0 else "N/A"
                        condition = parts[1].strip() if len(parts) > 1 else "N/A"
                    except:
                        size = "N/A"
                        condition = "N/A"

                    result = {
                        "name": name,
                        "price": price,
                        "image": img,
                        "brand": brand,
                        "size": size,
                        "condition": condition,
                        "link": link
                    }

                    new_results.append(result)

                except Exception as e:
                    print(f"Fehler beim Verarbeiten eines Items: {e}")

            if new_results:
                with open("data.json", "w", encoding="utf-8") as f:
                    json.dump(new_results, f, ensure_ascii=False, indent=3)
                print(f"{len(new_results)} neue Artikel gespeichert.")
            else:
                print("Keine neuen Artikel.")

        except Exception as e:
            print(f"Fehler beim Scrapen: {e}")

        time.sleep(60)


scraper_thread = threading.Thread(target=run_scraper)
scraper_thread.start()

bot.run(token)
