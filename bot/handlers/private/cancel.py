from aiogram import Router
from aiogram.types import Message
from fluentogram import TranslatorRunner

from bot.filters.message_chat_type import ChatType
from bot.filters.text import Text
from bot.handlers.keyboards.menu import get_menu_keyboard

router = Router()
router.message.filter(ChatType(is_group=False))


@router.message(Text("cancel"))
async def cancel(message: Message, i18n: TranslatorRunner):
    await message.answer(i18n.get("message-cancelled"), reply_markup=get_menu_keyboard(i18n))
