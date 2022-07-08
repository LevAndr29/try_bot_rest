from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
bot = Bot(token='5357463927:AAFvuTD7kCXTo7igf9PBzVQFvpQq_k5H1VI')
dp = Dispatcher(bot, storage=MemoryStorage())

async def error_stop(id_admin, text):
    await bot.send_message(id_admin, text)