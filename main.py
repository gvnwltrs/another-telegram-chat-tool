#!/usr/bin/env python3 

import asyncio
import json
from telegram import Bot

# Get config data
with open('config/my_telegram_config.json', 'r') as file:
    config_data = json.load(file)

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token
BOT_TOKEN = config_data['telegram_bot_token']

# Replace 'YOUR_CHAT_ID' with the chat ID you want to send the message to
CHAT_ID = config_data['api_key']

async def send_telegram_message(message):
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message)

# Example usage
# message_to_send = "Hello, Telegram!"
message_to_send = input()
asyncio.run(send_telegram_message(message_to_send))
