import os
import requests
import yfinance as yf

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_alert(message: str):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram credentials not set. Skipping alert.")
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            print(f"Failed to send Telegram alert: {response.text}")
    except Exception as e:
        print(f"Exception sending Telegram alert: {e}")

def load_universe():
    # Replace this with your own universe or ticker list source
    return ["AAPL", "MSFT", "GOOG"]

def get_price_data(ticker):
    try:
        data = yf.download(ticker, period="6mo", interval="1d")
        if data.empty:
            return None
        return data
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None
