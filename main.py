import os
import datetime
import requests

def send_photo(photo_path, caption):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("Missing Telegram credentials.")
        return

    url = f"https://api.telegram.org/bot{token}/sendPhoto"
    with open(photo_path, "rb") as photo:
        files = {"photo": photo}
        data = {"chat_id": chat_id, "caption": caption}
        response = requests.post(url, files=files, data=data)
        print(response.json())

def main():
    now = datetime.datetime.now()
    hour = now.hour

    print(f"Running at hour: {hour}")

    if hour == 6:
        send_photo("images/morning.jpg", "أذكار الصباح")
    elif hour == 18:
        send_photo("images/evening.jpg", "أذكار المساء")
    else:
        # تشغيل يدوي أو وقت غير معروف -> نبعت الزوز
        send_photo("images/morning.jpg", "أذكار الصباح")
        send_photo("images/evening.jpg", "أذكار المساء")

if __name__ == "__main__":
    main()
