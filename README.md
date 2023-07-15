# another-telegram-chat-tool

## Requirements
Install python-telegram-bot with:

```pip3 install python-telegram-bot```

How to Get Token and Chat ID
Make sure you have generated a Telegram chat bot first using something like 'BotFather'. If you have a generated bot, use the BotFather to find your token information.

Make sure that you've added your bot to your chat group and get your chat_id with:

```https://api.telegram.org/bot<YourBotToken>/getUpdates```

You just need to parse the json stuff to find the chat id for your bot name.