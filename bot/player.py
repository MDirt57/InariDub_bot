from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext

from bot.message_manager import MessageManager
import inject
from database.title_repository import TitleRepository
from dotenv import load_dotenv
import os


def player_keyboard(title_id, episode_pos):
    player_keyboard = [
        [
            InlineKeyboardButton("Попередня", callback_data=f"prev:-1:{title_id}") if episode_pos != -1 else InlineKeyboardButton(" ",
                                                                                                                    callback_data="none"),
            InlineKeyboardButton("Наступна", callback_data=f"next:1:{title_id}" if episode_pos != 1 else InlineKeyboardButton(" ", callback_data="none"))
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
    title_id = int(update.message.text.split()[1])
    video_id, desc = await get_episode_info(update, context, repository, title_id, 0)

    message = await context.bot.send_video(
        chat_id=update.message.chat_id,
        video=video_id,
        caption=desc,
        reply_markup=player_keyboard(title_id, MessageManager.is_first_or_last_episode(context, title_id, repository))
    )

    MessageManager.save_data(context, message.chat_id, message.message_id)


async def get_episode_info(update: Update, context: CallbackContext, repository: TitleRepository, title_id, increment):
    episode_number = MessageManager.get_current_episode_in_profile(context, title_id)
    chat_id, interface_id = MessageManager.load_data(context)
    episode = repository.get_episode(title_id, episode_number+increment)

    message = await context.bot.forwardMessage(
        chat_id=chat_id,
        from_chat_id="-1002488755396",
        message_id=episode.msg_id,
    )
    await context.bot.delete_message(chat_id=message.chat_id, message_id=message.message_id)

    return message.video.file_id, episode.description
