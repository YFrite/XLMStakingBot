import os

from pyrogram import Client
from dotenv import load_dotenv
from pyrogram.types import Message

load_dotenv(".env")
BOT_TOKEN = os.getenv("BOT_TOKEN")
APP_ID = os.getenv("APP_ID")
APP_HASH = os.getenv("APP_HASH")

print(APP_HASH)

app = Client(name="main_app",
             api_hash=APP_HASH,
             api_id=APP_ID,
             bot_token=BOT_TOKEN)


@app.on_message()
async def handler(client: Client, message: Message):
    await message.reply("Test")


if __name__ == "__main__":
    app.run()
