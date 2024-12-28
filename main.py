from telegram import Update
from telegram.ext import CallbackQueryHandler, ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os
from bot import navigation_keyboard
from database import di


load_dotenv()

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise "TOKEN not found"

application = ApplicationBuilder().token(TOKEN).build()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo("images/inari_logo.jpg", caption="Вас вітає Інарі-бот!", reply_markup=navigation_keyboard.menu)


if __name__ == '__main__':

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(navigation_keyboard.keyboard_tree))
    application.run_polling()

