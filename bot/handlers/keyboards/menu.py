from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from fluentogram import TranslatorRunner


async def menu_keyboard(i18n: TranslatorRunner):

    menu_builder = ReplyKeyboardBuilder()

    menu_builder.row(
        KeyboardButton(text=i18n.get("")),
        KeyboardButton(text=i18n.get(""))
    )

    menu_builder.row(
        KeyboardButton(text=i18n.get("...")),
        KeyboardButton(text=i18n.get("..."))
    )

    return menu_builder.as_markup(resize_keyboard=True, one_time_keyboard=False)
