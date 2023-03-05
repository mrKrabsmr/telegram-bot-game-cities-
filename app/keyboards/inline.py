from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def ikb_callback() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)
    alone = InlineKeyboardButton('Что за город?', callback_data='what_is_city')
    ikb.add(alone)

    return ikb
