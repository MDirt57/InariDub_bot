from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext

from bot.message_manager import MessageManager
import inject
from database.title_repository import TitleRepository
from dotenv import load_dotenv
import os


def player_keyboard(title_id, episode_pos, all_episodes, episode_type):
    player_keyboard = [
        [
            InlineKeyboardButton("Попередня", callback_data=f"prev:-1:{title_id}:{episode_type}") if episode_pos != 0 else InlineKeyboardButton(" ", callback_data="none"),
            InlineKeyboardButton("Наступна", callback_data=f"next:1:{title_id}:{episode_type}") if episode_pos != all_episodes else InlineKeyboardButton(" ", callback_data="none")
        ],
        [
            InlineKeyboardButton("На головну", callback_data="main"),
        ]
    ]

    return InlineKeyboardMarkup(player_keyboard)


load_dotenv()
TEST_VIDEO_ID = os.getenv("TEST_VIDEO_ID")


@inject.params(repository=TitleRepository)
async def send_video(update: Update, context: CallbackContext, repository: TitleRepository) -> None:
    episode_type = True if update.message.text.split()[0][1] == "d" else False
    title_id = int(update.message.text.split()[1])
    episode_number = MessageManager.get_current_episode_in_profile(context, title_id)
    episode, all_episodes_number = repository.get_episode(title_id, episode_number, episode_type)

    message = await context.bot.send_video(
        chat_id=update.message.chat_id,
        video=episode.bot_video_id,
        caption=episode.description,
        reply_markup=player_keyboard(title_id, episode_number, all_episodes_number, episode_type)
    )

    MessageManager.add_current_episode_in_profile(context, title_id, episode_number)
    MessageManager.save_data(context, message.chat_id, message.message_id)
