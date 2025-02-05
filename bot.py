import os
from dotenv import load_dotenv
from kucoin.client import Client
from kucoin.exceptions import KucoinAPIException

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
API_PASSPHRASE = os.getenv('API_PASSPHRASE')

# Initialize the KuCoin client
client = Client(API_KEY, API_SECRET, API_PASSPHRASE)

# Define the trading pair and strategy parameters
TRADING_PAIR = 'BTC-USDT'
INTERVAL = '1min'
QUANTITY = 0.001  # Adjust the quantity based on your needs
SMA_PERIOD = 14

def get_sma(symbol, interval, period):
    try:
        klines = client.get_kline_data(symbol, interval, period)
        closes = [float(kline[2]) for kline in klines]
        sma = sum(closes) / len(closes)
        return sma
    except Exception as e:
        print(f"Error fetching SMA: {e}")
        return None

def place_order(symbol, side, quantity):
    try:
        if side == 'buy':
            order = client.create_market_order(symbol, Client.SIDE_BUY, size=quantity)
        elif side == 'sell':
            order = client.create_market_order(symbol, Client.SIDE_SELL, size=quantity)
        print(f"Order placed: {order}")
    except KucoinAPIException as e:
        print(f"Error placing order: {e}")