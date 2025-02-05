import os
from dotenv import load_dotenv
from kucoin.client import Client
from kucoin.exceptions import KucoinAPIException
from flask import Flask, render_template, jsonify
from bot import client  # Import the client from bot.py

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def status():
    try:
        # Check connection by getting account information
        account_info = client.get_account()
        return jsonify({"status": "Connected", "account_info": account_info})
    except Exception as e:
        return jsonify({"status": f"Connection failed: {e}"})

if __name__ == '__main__':
    app.run(debug=True)