import requests
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN=os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID=os.getenv("TELEGRAM_CHAT_ID")


def send_telegram_message(message: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to send Telegram message: {e}")
