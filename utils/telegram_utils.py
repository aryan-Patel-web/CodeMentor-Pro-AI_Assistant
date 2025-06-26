from telegram import Bot
import os
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
user_id = int(os.getenv("TELEGRAM_USER_ID"))

def send_telegram_message(text):
    try:
        bot.send_message(chat_id=user_id, text=text)
    except Exception as e:
        print(f"Telegram text error: {e}")

def send_telegram_file(file_path, filename=None):
    try:
        with open(file_path, 'rb') as f:
            bot.send_document(chat_id=user_id, document=f, filename=filename or os.path.basename(file_path))
    except Exception as e:
        print(f"Telegram file error: {e}")
