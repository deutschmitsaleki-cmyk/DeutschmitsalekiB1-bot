import os
import json
import urllib.parse
import urllib.request
from datetime import date

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["B1_CHAT_ID"]

with open("topics_365_b1.json", encoding="utf-8") as f:
    topics = json.load(f)["topics"]

topic = topics[date.today().toordinal() % len(topics)]


def bullets(items):
    return "\n".join("• " + x.strip() for x in items)


message = f"""🇩🇪 Deutsch B1 – Tagesaufgabe #{topic["day"]}

📌 THEMA
{topic["title"]}

🗣 SPRECHEN
❓ {topic["speaking"]["questions"][0]}
❓ {topic["speaking"]["questions"][1]}

🎤 Aufgabe:
{topic["speaking"]["task"]}

✍️ SCHREIBEN
📄 Format: {topic["writing"]["format"]}
📏 Länge: {topic["writing"]["word_count"]}

📝 Aufgabe:
{topic["writing"]["task"]}

🔎 Achte auf:
{bullets(topic["writing"]["checklist"])}

📚 WORTSCHATZ
{bullets(topic["vocabulary"])}

🔹 REDEMITTEL
{bullets(topic["redemittel"])}

🧩 GRAMMATIK
{topic["grammar"]}

🇩🇪 Viel Erfolg!
"""

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

data = urllib.parse.urlencode({
    "chat_id": CHAT_ID,
    "text": message
}).encode()

with urllib.request.urlopen(url, data=data, timeout=30) as r:
    response = r.read().decode()
    print("TELEGRAM RESPONSE:")
    print(response)



