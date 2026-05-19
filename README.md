# Vinted Scraper Discord Bot

Ein Python-Bot, der neue Artikel von [Vinted](https://www.vinted.de) überwacht und automatisch in einen Discord-Kanal postet.

Dieses Projekt dient **nur zu Lernzwecken** und wird **nicht privat oder kommerziell genutzt**. Es ist ein Einstieg ins **Web-Scraping** und den Aufbau von Discord-Bots.

---

## ⚡ Features

- Scrapt Vinted regelmäßig nach neuen Artikeln
- Sendet Artikel-Informationen in einen Discord-Kanal:
  - Name
  - Preis
  - Größe
  - Marke
  - Zustand
  - Bild
- Enthält Buttons mit direkten Links zu den Angeboten
- Läuft mit **Selenium + ChromeDriver**
- Discord-Bot mit `discord.py`
- Verwendet `.env` für sichere Speicherung sensibler Daten
- Speichert bereits gefundene Artikel in `data.json`, um doppelte Posts zu vermeiden

---

## 📸 Beispiel

<img width="1188" height="903" alt="Screenshot 2026-01-18 152331" src="https://github.com/user-attachments/assets/44f11bd4-3e69-47ac-93b2-de12703b2134" />

---

## 🛠 Technologien

- Python
- Selenium
- ChromeDriver
- discord.py
- python-dotenv
- JSON

---

## 📦 Installation

### 1. Repository klonen

```bash
git clone https://github.com/ademragam/discord-bot-vinted-scraper.git
```

```bash
cd discord-bot-vinted-scraper
```

---

### 2. Python-Version prüfen

Stelle sicher, dass Python **3.10 oder neuer** installiert ist.

```bash
python --version
```

Falls dieser Befehl nicht funktioniert, nutze:

```bash
python3 --version
```

---

### 3. Virtuelle Umgebung erstellen

```bash
python -m venv venv
```

Virtuelle Umgebung aktivieren:

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

---

### 4. Benötigte Libraries installieren

Da in diesem Projekt keine `requirements.txt` vorhanden ist, können die benötigten Libraries manuell installiert werden:

```bash
pip install selenium discord.py python-dotenv
```

---

## 🔑 Umgebungsvariablen einrichten

Erstelle im Hauptordner des Projekts eine Datei mit dem Namen `.env`.

```env
DISCORD_TOKEN=dein_discord_bot_token
CHANNEL_ID=deine_channel_id
```

Ersetze die Werte durch deinen eigenen Discord-Bot-Token und die ID des Discord-Kanals, in den der Bot posten soll.

---

## 🚀 Bot starten

Nachdem alle Abhängigkeiten installiert und die `.env` Datei eingerichtet wurde, kann der Bot gestartet werden:

```bash
python bot.py
```

Falls du macOS oder Linux nutzt und `python` nicht funktioniert, nutze:

```bash
python3 bot.py
```

---

## 📁 Projektstruktur

```bash
discord-bot-vinted-scraper/
├── .env
├── LICENSE
├── README.md
├── bot.py
└── data.json
```

### Dateien kurz erklärt

- `.env`  
  Enthält sensible Daten wie den Discord-Bot-Token und die Channel-ID.

- `LICENSE`  
  Enthält die Lizenzinformationen des Projekts.

- `README.md`  
  Enthält die Dokumentation des Projekts.

- `bot.py`  
  Hauptdatei des Projekts. Hier befindet sich der Code für den Discord-Bot und das Scraping.

- `data.json`  
  Speichert bereits erkannte oder gepostete Artikel, damit sie nicht mehrfach gesendet werden.

---

## 🔐 Sicherheit

Der Discord-Bot-Token darf niemals öffentlich veröffentlicht werden.

Stelle sicher, dass deine `.env` Datei nicht auf GitHub hochgeladen wird. Dafür sollte sie in der `.gitignore` stehen:

```gitignore
.env
venv/
__pycache__/
```

Falls dein Token versehentlich auf GitHub hochgeladen wurde, solltest du ihn sofort im Discord Developer Portal zurücksetzen.

---

## ⚠️ Disclaimer

Dieses Projekt dient ausschließlich zu Lernzwecken.

Der Bot wird nicht privat oder kommerziell genutzt. Beim Web-Scraping sollten stets die Nutzungsbedingungen der jeweiligen Webseite beachtet werden. Dieses Projekt soll lediglich zeigen, wie man mit Python, Selenium und Discord-Bots arbeitet.

---

## 🧠 Was ich gelernt habe

In diesem Projekt wurden verschiedene Themen kombiniert:

- Aufbau eines Discord-Bots
- Arbeiten mit `discord.py`
- Nutzung von Selenium für Web-Scraping
- Extraktion von Artikeldaten aus Webseiten
- Umgang mit Umgebungsvariablen
- Speichern von Daten in einer JSON-Datei
- Strukturierung eines Python-Projekts
- Automatisches Senden von Nachrichten in Discord

---

## 📌 Mögliche Erweiterungen

- Filter nach Preis, Marke oder Größe
- Mehrere Suchbegriffe gleichzeitig überwachen
- Speicherung der Artikel mit Zeitstempel
- Bessere Fehlerbehandlung
- Logging einbauen
- Deployment auf einem Server
- Interaktive Discord-Commands hinzufügen
- `requirements.txt` ergänzen

---

## 👤 Autor

Erstellt von **Adem Ragam**

GitHub: [@ademragam](https://github.com/ademragam)

---

## 📄 Lizenz

Dieses Projekt ist unter der im Repository enthaltenen Lizenz verfügbar.
