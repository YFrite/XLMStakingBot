from bot.filters.private_message import PrivateMessage
from main import dp

if __name__ == "bot.filters":
    dp.filters_factory.bind(PrivateMessage)
