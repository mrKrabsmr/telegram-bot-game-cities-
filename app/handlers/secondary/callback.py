import asyncio

import wikipedia
from aiogram import types
from aiogram.dispatcher import FSMContext

from app.handlers.base.fsm import FSMPLayGame
from app.loader import dp


@dp.callback_query_handler(lambda call: call.data.startswith('accept'), state=[FSMPLayGame.start, FSMPLayGame.name])
async def city_callback(callback: types.CallbackQuery, state=FSMContext):
    city = callback.data.split(':')[-1]
    try:
        wikipedia.set_lang('ru')
        result = wikipedia.summary(city, sentences=4).split('==')
        msg = await callback.message.answer(result[0])
        await callback.answer()
        await asyncio.sleep(15)
        await msg.delete()
    except Exception as e:
        await callback.answer('☹️ Не нашел информацию об этом городе', show_alert=True)
