from telegram import Update
from telegram.ext import (CallbackQueryHandler, ApplicationBuilder, MessageHandler, filters, CallbackContext,
                          CommandHandler, ContextTypes, InlineQueryHandler)
from dotenv import load_dotenv
import os
from bot import navigation_keyboard
from bot import title_list
from bot.message_manager import MessageManager
from database import di
from bot import player
from bot.channel_handler import handle_channel_post
from bot.keyboard_tree import keyboard_tree


load_dotenv()

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise "TOKEN not found"

application = ApplicationBuilder().token(TOKEN).build()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    MessageManager.save_data(context, update.message.chat_id, 0)
    await MessageManager.return_main(update, context)

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.message)

if __name__ == '__main__':

    application.add_handler(CommandHandler("start", start))
    # application.add_handler(CommandHandler("s", player.send_video))
    application.add_handler(CommandHandler("t", player.send_video))
    application.add_handler(MessageHandler(filters.ALL, handle_channel_post))
    # application.add_handler(MessageHandler(filters.ALL, info))

    # application.add_handler(CommandHandler("title", title))
    application.add_handler(InlineQueryHandler(title_list.title_list))
    application.add_handler(CallbackQueryHandler(keyboard_tree))
    application.run_polling(allowed_updates=Update.ALL_TYPES)

