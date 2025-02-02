from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaVideo
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



