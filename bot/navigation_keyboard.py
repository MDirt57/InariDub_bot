from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaVideo
from telegram.ext import ContextTypes
import random
import inject
from database.title_repository import TitleRepository
from bot.message_manager import MessageManager

menu_keyboard = [
    [
        InlineKeyboardButton("Моя нора", callback_data="myprofile"),
        InlineKeyboardButton("Пошук тайтлів", callback_data="search_titles")
    ],
    [
        InlineKeyboardButton("List Test", callback_data="list_test"),
        InlineKeyboardButton("Temp2", callback_data="temp2")
    ],
    [
        InlineKeyboardButton("Test", callback_data="test"),
    ]
]
menu = InlineKeyboardMarkup(menu_keyboard)

sub_dub_keyboard = [
    [
        InlineKeyboardButton("Саб", switch_inline_query_current_chat="s:"),
        InlineKeyboardButton("Даб", switch_inline_query_current_chat="d:")
    ],
    [
        InlineKeyboardButton("Повернутись", callback_data="back"),
    ]
]
sub_dub = InlineKeyboardMarkup(sub_dub_keyboard)


