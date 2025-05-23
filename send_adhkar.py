import os
import requests

def send_dhikr():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("Missing Telegram credentials.")
        return

    text = "لَا إلَهَ إلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ، لَهُ المُلكُ ولَهُ الحمدُ يُحيِي ويُميتُ وهو علَى كلِّ شيءٍ قدير"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    response = requests.post(url, data=data)
    print(response.json())

if __name__ == "__main__":
    send_dhikr()
