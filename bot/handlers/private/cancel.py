from aiogram import Router
from aiogram.types import Message
from fluentogram import TranslatorRunner

from bot.filters.text import Text

router = Router()


@router.message(Text("Cancel"))
async def cancel(message: Message, i18n: TranslatorRunner):
    await message.answer(i18n.get("Cancelled"))
