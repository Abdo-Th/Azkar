import os
import datetime
from telegram import Bot

bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")

bot = Bot(token=bot_token)

now = datetime.datetime.utcnow()
hour = now.hour

image_path = "azkar_sabah.jpg" if hour == 6 else "azkar_masaa.jpg"

with open(image_path, 'rb') as photo:
    bot.send_photo(chat_id=chat_id, photo=photo)
