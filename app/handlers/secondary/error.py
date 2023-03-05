from aiogram import types

from app.loader import dp


@dp.errors_handler()
async def error_all(message: types.Message):
    await message.answer(text='Извините, что-то пошло не так...')
