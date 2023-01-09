from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from fluentogram import TranslatorRunner

from bot.filters.message_chat_type import ChatType
from bot.filters.text import Text

router = Router()
router.message.filter(ChatType(False))


@router.message(Command("start"))
async def test(message: Message, i18n: TranslatorRunner):
    await message.answer(i18n.get("Hello"))


@router.message(Text("Credentials"))
async def test(message: Message, i18n: TranslatorRunner):
    await message.answer(i18n.get("Cr"))
