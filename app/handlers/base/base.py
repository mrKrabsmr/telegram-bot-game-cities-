import hashlib
from time import sleep

import wikipedia
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.handlers.base.fsm import FSMPLayGame
from app.handlers.base.utils import game_func_one, game_func_two, game_func_three, game_func_four, game_func_five
from app.keyboards.simple import stop, start_keyboard, end_win_game_kb
from app.loader import dp


@dp.message_handler(text='Начать игру', state=FSMPLayGame.start)
async def start_game(message: types.Message, state=FSMContext):
    msg_one = await message.answer('Начинаем игру через:')
    n = 3
    for _ in range(3):
        msg_two = await message.answer(n)
        sleep(1)
        await msg_two.delete()
        n -= 1
    await msg_one.delete()
    city = game_func_three()
    async with state.proxy() as proxy:
        proxy[f'{city[-1]}'] = True
    ikb = InlineKeyboardMarkup(row_width=1)
    alone = InlineKeyboardButton('Что за город?', callback_data=f'accept:{city[-1]}')
    ikb.add(alone)
    await message.answer(f'Первый город: {city[-1]}', reply_markup=ikb)
    await FSMPLayGame.name.set()


@dp.message_handler(text='Стоп игра', state=FSMPLayGame)
async def stop_game(message: types.Message, state=FSMContext):
    if message.from_user.username is not None:
        game_func_five(message.from_user.username)
    else:
        game_func_five(message.from_user.full_name)
    await message.answer('Завершаем игру')
    sleep(2)
    async with state.proxy() as proxy:
        await message.answer(f'Результат: {len(list(proxy.as_dict().keys())) // 2}/30',
                             reply_markup=start_keyboard())
    await state.finish()


@dp.message_handler(text='Завершить обзор игры', state=FSMPLayGame)
async def end_win_game(message: types.Message, state=FSMContext):
    if message.from_user.username is not None:
        game_func_four(message.from_user.username)
    else:
        game_func_four(message.from_user.full_name)
    await message.answer('Спасибо за игру и до скорой встречи!', reply_markup=start_keyboard())
    await state.finish()


@dp.message_handler(state=FSMPLayGame.name)
async def go_game(message: types.Message, state=FSMContext):
    async with state.proxy() as proxy:
        if message.text[0].lower() != list(proxy.as_dict().keys())[-1][-1]:
            await message.reply('Неправильно! Перечитайте правила игры', reply_markup=stop())
        elif message.text.capitalize() in list(proxy.as_dict().keys()):
            await message.reply('Такой город уже был!', reply_markup=stop())
        elif not game_func_two(message.text):
            await message.reply('Я не знаю о таком городе!', reply_markup=stop())
        else:
            if game_func_one(message.text):
                if len(list(proxy.as_dict().keys())) // 2 == 28:
                    await message.answer('Невероятно! 30 названных городов!\n'
                                         'Сегодня я проиграл, признаю, ты был хорош 😒', reply_markup=end_win_game_kb())
                else:
                    bot_ans = game_func_one(message.text)
                    proxy[f'{message.text.capitalize()}'] = True
                    proxy[f'{bot_ans.capitalize()}'] = True
                    ikb = InlineKeyboardMarkup(row_width=1)
                    alone = InlineKeyboardButton('Что за город?', callback_data=f'accept:{bot_ans}')
                    ikb.add(alone)
                    await message.reply(text=bot_ans, reply_markup=ikb)
            else:
                await message.reply(text=f'Я не знаю город на букву {message.text[-1]}', reply_markup=stop())
    await FSMPLayGame.name.set()


@dp.inline_handler()
async def with_wiki(query: types.InlineQuery):
    text = query.query or 'echo'
    wikipedia.set_lang('ru')
    try:
        result = wikipedia.page(title='город ' + query.query)
    except Exception:
        result = wikipedia.page(title='Лос-Анджелес')
    f = types.InputMessageContent(message_text=result.url)
    articles = [types.InlineQueryResultArticle(
        id='seccccrettaeuioase',
        title=f'Город {query.query}',
        url=result.url,
        input_message_content=f
    )]
    await query.answer(articles, cache_time=1, is_personal=True)
