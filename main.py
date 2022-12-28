import os

from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv(".env")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SKIP_UPDATES = bool(os.getenv("SKIP_UPDATES"))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


async def startup(dispatcher: Dispatcher):
    pass

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=startup, skip_updates=SKIP_UPDATES)
