from telegram import Update, InputMediaVideo
from telegram.ext import ContextTypes
import random
import inject
from database.title_repository import TitleRepository
from bot.message_manager import MessageManager
from bot.navigation_keyboard import menu, sub_dub
from bot.player import player_keyboard

@inject.params(repository=TitleRepository)
async def keyboard_tree(update: Update, context: ContextTypes.DEFAULT_TYPE, repository: TitleRepository):
    query = update.callback_query
    await query.answer()

    if query.data == "titles":
        await query.edit_message_caption(caption=str([title.name for title in repository.get_all_titles()[:5]]),
                                         reply_markup=menu)
    elif query.data == "main":
        await MessageManager.delete_interface(context)

        await MessageManager.return_main(update, context)

    elif query.data == "back":
        await query.edit_message_reply_markup(reply_markup=menu)

    elif query.data == "search_titles":
        await query.edit_message_reply_markup(reply_markup=sub_dub)

    elif query.data.split(":")[0] == "next" or query.data.split(":")[0] == "prev":
        episode_type = bool(query.data.split(":")[3] == "True")
        title_id = query.data.split(":")[2]
        increment = int(query.data.split(":")[1])
        episode_number = MessageManager.get_current_episode_in_profile(context, title_id) + increment
        episode, all_episodes_number = repository.get_episode(title_id, episode_number, episode_type)
        await query.edit_message_media(
            media=InputMediaVideo(
                media=episode.bot_video_id,
                caption=episode.description,
            ),
            reply_markup=player_keyboard(title_id, episode_number, all_episodes_number, episode_type)
        )
        MessageManager.add_current_episode_in_profile(context, title_id, MessageManager.get_current_episode_in_profile(context, title_id)+increment)

    elif query.data == "none":
        pass

    elif query.data == "test":
        pass
    else:
        pass