from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext

from bot.message_manager import MessageManager
import inject
from database.title_repository import TitleRepository
from dotenv import load_dotenv
import os

player_keyboard = [
    [
        InlineKeyboardButton("Попередня", callback_data="prev"),
        InlineKeyboardButton("Наступна", callback_data="next")
    ],
    [
        InlineKeyboardButton("На головну", callback_data="main"),
    ]
]

player = InlineKeyboardMarkup(player_keyboard)

load_dotenv()
TEST_VIDEO_ID = os.getenv("TEST_VIDEO_ID")

@inject.params(repository=TitleRepository)
async def send_video(update: Update, context: CallbackContext, repository: TitleRepository) -> None:
    full_name = update.message.text[3:]

    await context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    await MessageManager.delete_interface(context)

    message = await context.bot.send_video(
        chat_id=update.message.chat_id,
        video=TEST_VIDEO_ID,
        caption=repository.get_full_info(full_name).name,
        reply_markup = player
    )

    MessageManager.save_data(context, message.chat_id, message.message_id)





