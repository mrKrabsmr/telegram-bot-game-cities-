from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from secret_data.config import TOKEN_API

bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot, storage=MemoryStorage())

