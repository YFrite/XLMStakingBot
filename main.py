import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from fluent_compiler.bundle import FluentBundle
from fluentogram import TranslatorHub, FluentTranslator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from bot.handlers.private import about, cancel
from bot.middlewares.translator import TranslatorMiddleware
from db.models.base import Base
from di.container import Container


async def main():

    # Config
    load_dotenv(".env")
    bot_token = os.getenv("BOT_TOKEN")
    skip_updates = bool(os.getenv("SKIP_UPDATES"))
    database_url = os.getenv("DATABASE_URL")

    # Database setup (In this case - SQLAlchemy)
    database_engine = create_async_engine(database_url)
    session = async_sessionmaker(database_engine, expire_on_commit=False, autoflush=True)
    async with database_engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    # Setup DI
    container = Container()
    container.config.set("session", session())

    # Bot initialization
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
    try:
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        await database_engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
