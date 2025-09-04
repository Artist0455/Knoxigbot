import os
from telegram.ext import ApplicationBuilder, CommandHandler

# Load environment variables
load_dotenv()

from bot.handlers.start_handler import start_handler
from bot.handlers.message_handler import message_save_handler
from bot.handlers.history_handler import allhistory_handler

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if __name__ == '__main__':
    app = ApplicationBuilder().token("YOUR_TOKEN").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(message_save_handler)
    app.add_handler(allhistory_handler)

    print("🚀 Knox Bot is running...")
    app.run_polling()

