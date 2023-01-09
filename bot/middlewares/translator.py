from typing import Callable, Dict, Any, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message, CallbackQuery
from fluentogram import TranslatorHub


class TranslatorMiddleware(BaseMiddleware):
    def __init__(self, translator_hub: TranslatorHub):
        self.translator_hub = translator_hub

    async def __call__(self, handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: Union[Message, CallbackQuery],
                       data: Dict[str, Any]) -> Any:
        data["i18n"] = self.translator_hub.get_translator_by_locale(event.from_user.language_code)

        return await handler(event, data)
