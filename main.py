import datetime
import requests
import os

def send_photo(photo_path, caption):
    token = os.environ['TELEGRAM_BOT_TOKEN']
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    url = f"https://api.telegram.org/bot{token}/sendPhoto"
    with open(photo_path, 'rb') as photo:
        files = {'photo': photo}
        data = {'chat_id': chat_id, 'caption': caption}
        response = requests.post(url, files=files, data=data)
    return response

def main():
    now = datetime.datetime.now()
    hour = now.hour
    if hour == 6:
        send_photo('images/morning.jpg', 'أذكار الصباح')
    elif hour == 18:
        send_photo('images/evening.jpg', 'أذكار المساء')

if __name__ == "__main__":
    main()
