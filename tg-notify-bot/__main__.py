import os
import logging

from sys import exit

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils import exceptions as aio_exceptions

TG_TOKEN = os.getenv("TG_TOKEN")

logging.basicConfig(level="INFO", format="%(asctime)s %(levelname)s: %(message)s")
logger = logging.getLogger("TelegramNotifyBot")

try:
    bot = Bot(token=TG_TOKEN)
except aio_exceptions.ValidationError as error:
    logger.error("No environment variable TG_TOKEN provided")
    exit(1)

dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):
    await message.reply("I will notify you when recieve a message")


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
        "/help - print this message\n/start - initiate bot\n/chat_id - returns the id of this chat"
    )


if __name__ == "__main__":
    executor.start_polling(dp)
