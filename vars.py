import os

API_ID    = os.environ.get("API_ID", "29795810")
API_HASH  = os.environ.get("API_HASH", "3f6d609ea9d8367d8317e869bd8c0bb2")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7545335361:AAFplyJ6p2sUwh0euJiJZym9ZRZ8-DL3Dn0") 
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
