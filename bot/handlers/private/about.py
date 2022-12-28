from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from bot.filters.private_message import PrivateMessage
from main import dp


@dp.message_handler(Command("teest"), PrivateMessage())
async def test(message: Message):
    await message.reply("test")
