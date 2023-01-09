from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

cancel_builder = ReplyKeyboardBuilder()

cancel_builder.row(
    KeyboardButton(text=_("Cancel"))
)

menu = cancel_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
