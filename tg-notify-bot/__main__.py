import os
import logging

from sys import exit

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils import exceptions as aio_exceptions
from discord_webhook import DiscordWebhook, DiscordEmbed

TG_TOKEN = os.getenv("TG_TOKEN")
DS_WEBHOOK_URL=os.getenv("DS_WEBHOOK_URL")

logging.basicConfig(level="INFO", format="%(asctime)s %(levelname)s: %(message)s")
logger = logging.getLogger("TelegramNotifyBot")


bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):
    await message.reply("I will notify you when recieve a message")


@dp.message_handler(commands=["who"])
async def process_start_command(message: types.Message):
    user_name = message.from_user.username
    user_id = message.from_user.id

    chat = None
    if message.chat.type == "private":
        chat = f"private chat (id:{message.chat.id})"
    elif message.chat.type == "group":
        chat = f"Group: {message.chat.title} ({message.chat.id})"
    elif message.chat.type == "supergroup":
        chat = f"Supergroup: {message.chat.title} ({message.chat.id})"
    elif message.chat.type == "channel":
        chat = f"Channel: {message.chat.title} ({message.chat.id})"

    logger.info(f"Command: /who; User: {user_name} ({user_id}); From: {chat}")

    description = f"User: {message.from_user.username} ({message.from_user.id});\n" \
                  f"From: {chat}"
    embed = DiscordEmbed(description=description, color='03b2f8')
    webhook = DiscordWebhook(url=DS_WEBHOOK_URL, content="!who")
    webhook.add_embed(embed)
    webhook.execute()


@dp.message_handler(commands=["chat_id"])
async def process_info_command(message: types.Message):
    try:
        chat_id = str(message["chat"]["id"])
    except KeyError as er:
        logger.error(f"Cannot get chat_id: {er}")
        chat_id = "Cannot get chat id"
    await message.reply("chat_id: " + chat_id)


@dp.message_handler(commands=["help"])
async def process_help_command(message: types.Message):
    await message.reply(
        f"/help - print this message\n"
        f"/start - initiate bot\n"
        f"/chat_id - returns the id of this chat\n"
        f"/who - returns the active users on Discord Server"
    )


if __name__ == "__main__":
    executor.start_polling(dp)
