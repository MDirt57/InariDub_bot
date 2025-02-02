from telegram.ext import CallbackContext
from telegram import Update


async def handle_channel_post(update: Update, context: CallbackContext) -> None:
    if update.channel_post:
        text = update.channel_post.text
        chat_id = update.channel_post.chat_id
        # video_id = update.channel_post.video.file_id
        print(text, chat_id)
        ## add new item into database
