from telegram import Update, InputMediaVideo
from telegram.ext import ContextTypes
import random
import inject
from database.title_repository import TitleRepository
from bot.message_manager import MessageManager
from bot.navigation_keyboard import menu
from bot.player import get_episode_info, player_keyboard

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
    elif query.data.split(":")[0] == "next" or query.data.split(":")[0] == "prev":
        title_id = query.data.split(":")[2]
        increment = int(query.data.split(":")[1])
        video_id, desc = await get_episode_info(update, context, repository, title_id, increment)
        await query.edit_message_media(
            media=InputMediaVideo(
                media=video_id,
                caption=desc
            ),
            reply_markup=player_keyboard(title_id, MessageManager.is_first_or_last_episode(context, title_id, repository))
        )
        MessageManager.add_current_episode_in_profile(context, title_id, MessageManager.get_current_episode_in_profile(context, title_id)+increment)

    elif query.data == "none":
        pass
    else:
        pass