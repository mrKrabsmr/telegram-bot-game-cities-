from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def start_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    first = KeyboardButton('Мой профиль')
    second = KeyboardButton('ТОП игроков')
    third = KeyboardButton('/play')
    kb.add(first).add(second).add(third)

    return kb


def keyboard_play() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    start_game = KeyboardButton('Начать игру')
    not_game = KeyboardButton('Назад')
    kb.add(start_game).add(not_game)

    return kb


def stop() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    stop_ = KeyboardButton('Стоп игра')
    kb.add(stop_)

    return kb


def end_win_game_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    end = KeyboardButton('Завершить обзор игры')
    kb.add(end)

    return kb
