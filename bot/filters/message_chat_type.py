from typing import Union

from aiogram.filters import BaseFilter
from aiogram.types import Message


class ChatType(BaseFilter):
    __slots__ = "is_group"

    def __init__(self, is_group: bool):
        self.is_group = is_group

    async def __call__(self, message: Message) -> bool:
        return self.is_group != (message.chat.type == "private")
