from telegram import Update
from telegram.ext import MessageHandler, ContextTypes, filters
import os
from .message_handler import get_user_history
from dotenv import load_dotenv

load_dotenv()
BOT_USERNAME = os.getenv("BOT_USERNAME")

async def handle_allhistory(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text
    if not message_text.lower().startswith(f"@{BOT_USERNAME.lower()} allhistory"):
        return

    parts = message_text.split()
    if len(parts) < 3:
        await update.message.reply_text("❌ Usage: @Knoxsgbot allhistory <user_id>")
        return

    try:
        user_id = int(parts[2])
    except ValueError:
        await update.message.reply_text("❌ Invalid user ID format.")
        return

    user_history = get_user_history()
    history = user_history.get(user_id, [])
    if not history:
        await update.message.reply_text("📭 No history found for this user.")
    else:
        history_text = "\n".join(f"• {msg}" for msg in history[-10:])  # Last 10
        await update.message.reply_text(f"🕘 Last messages from {user_id}:\n\n{history_text}")

allhistory_handler = MessageHandler(filters.TEXT & filters.ChatType.GROUPS, handle_allhistory)
