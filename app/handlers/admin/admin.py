from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from app.container import city_service
from app.handlers.admin.utils import check_is_in_db, check_is_admin
from app.handlers.secondary.text import admin_add_text
from app.loader import dp


class FSMAdminPlay(StatesGroup):
    city = State()


@dp.message_handler(commands=['admin'])
async def sm_start(message: types.Message):
    if check_is_admin(message.from_user):
        await FSMAdminPlay.city.set()
        await message.answer(text=admin_add_text, parse_mode=types.ParseMode.HTML)
    else:
        await message.answer('Вы не являетесь админом, следовательно, эта функция вам недоступна')


@dp.message_handler(text='Готово', state=FSMAdminPlay.city)
async def end_add(message: types.Message, state=FSMContext):
    await message.answer('Успешно добавлено')
    await state.finish()


@dp.message_handler(content_types=['text'], state=FSMAdminPlay.city)
async def add_city(message: types.Message, state=FSMContext):
    if check_is_in_db(message.text):
        await message.answer('Такой город уже есть в базе данных')
    else:
        city_service.create(message.text)
    await FSMAdminPlay.city.set()
