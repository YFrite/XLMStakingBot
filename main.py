import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.utils.i18n import I18n, SimpleI18nMiddleware
from dotenv import load_dotenv

from bot.handlers.private import about


async def main():

    # Bot initialization
    load_dotenv(".env")
    bot_token = os.getenv("BOT_TOKEN")
    skip_updates = bool(os.getenv("SKIP_UPDATES"))

    bot = Bot(token=bot_token)
    dp = Dispatcher()

    # Localization
    i18n = I18n(path="locales", default_locale="en", domain="messages")
    dp.message.middleware(SimpleI18nMiddleware(i18n=i18n, i18n_key="messages", middleware_key="i18n_messages"))

    # Routes
    dp.include_router(router=about.router)

    # Launching
    await bot.delete_webhook(drop_pending_updates=skip_updates)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
