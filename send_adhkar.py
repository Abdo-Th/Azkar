import requests
import os

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    response = requests.post(url, data=data)
    print(response.text)

# الدعاء المراد إرساله
adhkar = "لَا إِلَهَ إِلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ، لَهُ المُلكُ ولَهُ الحمدُ يُحيِي ويُميتُ وهو علَى كلِّ شيءٍ قدير"
send_telegram_message(adhkar)
