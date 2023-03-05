from aiogram import types
from aiogram.dispatcher import FSMContext

from app.container import user_service
from app.handlers.base.fsm import FSMPLayGame
from app.handlers.client.utils import add_new_user_to_db, my_profile_txt, top_users_txt
from app.handlers.secondary.text import start_text, help_text, play_text
from app.keyboards.simple import keyboard_play, start_keyboard
from app.loader import dp, bot


@dp.message_handler(commands=['start', 'help'])
async def main_commands(message: types.Message):
    if message.text == '/start':
        await message.answer(text=start_text,
                             reply_markup=start_keyboard(), parse_mode=types.ParseMode.HTML)
        if message.from_user.username is None:
            add_new_user_to_db(message.from_user.full_name)
        else:
            add_new_user_to_db(message.from_user.username)
    elif message.text == '/help':
        await message.answer(text=help_text)


@dp.message_handler(text='Мой профиль')
async def my_profile(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=my_profile_txt(message),
                           parse_mode=types.ParseMode.HTML)


@dp.message_handler(text='ТОП игроков')
async def top_users(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=top_users_txt())


@dp.message_handler(commands=['play'])
async def play_command(message: types.Message):
    await message.answer(text=play_text,
                         reply_markup=keyboard_play(),
                         parse_mode=types.ParseMode.HTML)
    await FSMPLayGame.start.set()


@dp.message_handler(text='Назад', state=FSMPLayGame.start)
async def not_game(message: types.Message, state=FSMContext):
    await message.answer(text='ок', reply_markup=start_keyboard())
    await state.finish()


@dp.message_handler()
async def everything_not_used(message: types.Message):
    await message.answer('Я не знаю, как на это отвечать')
