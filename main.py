import requests
import os
from datetime import datetime

BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

now = datetime.now()
hour = now.hour

# نحدد الصباح أو المساء حسب الوقت
if 3 <= hour < 15:
    IMAGE_PATH = 'images/morning.jpg'
    MESSAGE = "أذكار الصباح | صباح الخير"
else:
    IMAGE_PATH = 'images/evening.jpg'
    MESSAGE = "أذكار المساء | مساء الخير"

def send_photo():
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto'
    with open(IMAGE_PATH, 'rb') as photo:
        response = requests.post(url, data={
            'chat_id': CHAT_ID,
            'caption': MESSAGE
        }, files={'photo': photo})
    print(response.text)

if __name__ == "__main__":
    send_photo()
