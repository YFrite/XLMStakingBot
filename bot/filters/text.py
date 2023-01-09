from aiogram.filters import BaseFilter
from aiogram.types import Message
from fluentogram import TranslatorRunner


class Text(BaseFilter):

    __slots__ = "text"

    def __init__(self, text: str):
        self.text = text

    async def __call__(self, message: Message, i18n: TranslatorRunner) -> bool:
        return message.text == i18n.get(self.text)
