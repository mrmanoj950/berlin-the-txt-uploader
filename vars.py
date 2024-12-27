import os

API_ID    = os.environ.get("API_ID", "29795810")
API_HASH  = os.environ.get("API_HASH", "3f6d609ea9d8367d8317e869bd8c0bb2")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8091524070:AAHvYc-J0OvUUnBYB1-swnNO8AFEYpnCRIk") 
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
