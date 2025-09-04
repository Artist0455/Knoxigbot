from telegram import Update
from telegram.ext import MessageHandler, ContextTypes, filters

# In-memory user message store
user_history = {}

async def handle_group_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        user_id = update.message.from_user.id
        text = update.message.text

        if user_id not in user_history:
            user_history[user_id] = []

        user_history[user_id].append(text)

message_save_handler = MessageHandler(filters.TEXT & filters.ChatType.GROUPS, handle_group_messages)

# Export user_history so it can be used in other handlers
def get_user_history():
    return user_history
