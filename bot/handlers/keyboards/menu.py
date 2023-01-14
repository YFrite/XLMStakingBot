from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from fluentogram import TranslatorRunner


def get_menu_keyboard(i18n: TranslatorRunner):

    menu_builder = ReplyKeyboardBuilder()

    menu_builder.row(
        KeyboardButton(text=i18n.get("wallet")),
        KeyboardButton(text=i18n.get("staking"))
    )

    menu_builder.row(
        KeyboardButton(text=i18n.get("partners")),
        KeyboardButton(text=i18n.get("settings"))
    )

    return menu_builder.as_markup(resize_keyboard=True, one_time_keyboard=False)
