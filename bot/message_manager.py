from bot import navigation_keyboard

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



