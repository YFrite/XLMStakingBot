from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _

from bot.filters.message_chat_type import ChatType

router = Router()
router.message.filter(ChatType(False))


@router.message(Command("start"))
async def test(message: Message):
    await message.answer(_("Hi, i'm bot for staking XLM (Lumen)"))


@router.message(Command("credentials"))
async def test(message: Message):
    await message.answer(_("I was made by YFrite"))
