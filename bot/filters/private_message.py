from aiogram.dispatcher.filters import Filter
from aiogram.types import Message, ChatType


class PrivateMessage(Filter):
    key = "is_private_message"

    async def check(self, message: Message) -> bool:
        return message.chat.type == ChatType.PRIVATE
