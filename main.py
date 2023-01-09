import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from fluent_compiler.bundle import FluentBundle
from fluentogram import TranslatorHub, FluentTranslator

from bot.handlers.private import about, cancel
from bot.middlewares.translator import TranslatorMiddleware


async def main():

    # Bot initialization
    load_dotenv(".env")
    bot_token = os.getenv("BOT_TOKEN")
    skip_updates = bool(os.getenv("SKIP_UPDATES"))

    bot = Bot(token=bot_token)
    dp = Dispatcher()

    # Localization
    translator_hub = TranslatorHub(
        {"ru": ("ru", "en"),
         "en": ("en", "ru")
         },
        [
            FluentTranslator("en", translator=FluentBundle.from_files("en",
                                                                      filenames=["locales/en.ftl"])),
            FluentTranslator("ru", translator=FluentBundle.from_files("ru",
                                                                      filenames=["locales/ru.ftl"]))
        ]
    )
    dp.message.outer_middleware(TranslatorMiddleware(translator_hub=translator_hub))

    # Routes
    dp.include_router(router=about.router)
    dp.include_router(router=cancel.router)

    # Launching
    await bot.delete_webhook(drop_pending_updates=skip_updates)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
