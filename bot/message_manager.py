from bot import navigation_keyboard
from database.title_repository import TitleRepository


class MessageManager:


    @staticmethod
    async def return_main(update, context):
        message = await context.bot.send_photo(
            chat_id=context.user_data["chat_id"],
            photo=open("images/inari_logo.jpg", "rb"),
            caption="Вас вітає Інарі-бот!",
            reply_markup=navigation_keyboard.menu
        )
        MessageManager.save_data(context, message.chat_id, message.message_id)


    @staticmethod
    def save_data(context, chat_id, message_id):
        context.user_data["chat_id"] = chat_id
        context.user_data["interface_message_id"] = message_id

    @staticmethod
    def load_data(context):
        return context.user_data["chat_id"], context.user_data["interface_message_id"]

    @staticmethod
    async def delete_interface(context):
        await context.bot.delete_message(context.user_data["chat_id"], context.user_data["interface_message_id"])

    @staticmethod
    def add_current_episode_in_profile(context, title_id, episode_number):
        context.user_data[f"t:{title_id}"] = episode_number

    @staticmethod
    def get_current_episode_in_profile(context, title_id):
        try:
            return context.user_data[f"t:{title_id}"]
        except KeyError:
            return 1

    @staticmethod
    def is_first_or_last_episode(context, title_id, repository: TitleRepository):
        current_episode = MessageManager.get_current_episode_in_profile(context, title_id)
        if current_episode == 0:
            return -1
        elif current_episode == repository.get_title_info(title_id).series_count:
            return 1
        else:
            return 0