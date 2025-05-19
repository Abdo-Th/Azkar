import os
import requests
import random
from datetime import datetime

def send_telegram_photo(folder):
    token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['CHAT_ID']
    image_dir = f"images/{folder}"
    
    # اختيار صورة عشوائية من المجلد
    images = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.png'))]
    if not images:
        print("No images found!")
        return
    
    selected_image = random.choice(images)
    image_path = os.path.join(image_dir, selected_image)
    
    # إرسال الصورة
    url = f"https://api.telegram.org/bot{token}/sendPhoto"
    with open(image_path, 'rb') as photo:
        files = {'photo': photo}
        data = {'chat_id': chat_id}
        response = requests.post(url, files=files, data=data)
    
    print(f"Sent {folder} image: {selected_image}")

# تحديد الوقت الحالي (UTC)
current_hour = datetime.utcnow().hour

if 3 <= current_hour < 15:  # 6 صباحًا بتوقيت السعودية (UTC+3)
    send_telegram_photo("morning")
else:  # 6 مساءً بتوقيت السعودية
    send_telegram_photo("evening")
