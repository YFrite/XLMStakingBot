from aiogram import Router
from aiogram.filters import CommandStart, CommandObject
from aiogram.types import Message
from aiogram.utils.deep_linking import decode_payload
from dependency_injector.wiring import inject, Provide
from fluentogram import TranslatorRunner

from bot.filters.message_chat_type import ChatType
from bot.filters.text import Text
from bot.handlers.keyboards.menu import get_menu_keyboard
from db.repositories.user import UserRepository
from di.container import Container

router = Router()
router.message.filter(ChatType(is_group=False))


@router.message(CommandStart())
@inject
async def start(message: Message, command: CommandObject, i18n: TranslatorRunner,
                user_repository: UserRepository = Provide[Container.user_repository]):
    user_id = message.from_user.id

    if await user_repository.is_exists(user_id=user_id):
        await message.answer(i18n.get("message-menu"), reply_markup=get_menu_keyboard(i18n))
        return

    command_args = command.args
    if command_args:
        parent_id = int(decode_payload(command.args))
    else:
        parent_id = None

    await user_repository.add(user_id, parent_id=parent_id)
    await message.answer(i18n.get("message-hello"), reply_markup=get_menu_keyboard(i18n))


@router.message(Text("credentials"))
async def credentials(message: Message, i18n: TranslatorRunner):
    await message.answer(i18n.get("message-credentials"))
