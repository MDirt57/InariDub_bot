from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import random
import inject
from database.title_repository import TitleRepository
from bot.message_manager import MessageManager

menu_keyboard = [
    [
        InlineKeyboardButton("Моя нора", callback_data="myprofile"),
        InlineKeyboardButton("Пошук тайтлів", switch_inline_query_current_chat="t:")
    ],
    [
        InlineKeyboardButton("List Test", callback_data="list_test"),
        InlineKeyboardButton("Temp2", callback_data="temp2")
    ],
    [
        InlineKeyboardButton("Temp3", callback_data="temp3"),
    ]
]
menu = InlineKeyboardMarkup(menu_keyboard)


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
    else:
        await query.edit_message_caption(caption=str(random.randint(1, 6)), reply_markup=menu)
