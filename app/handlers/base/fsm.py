from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMPLayGame(StatesGroup):
    start = State()
    name = State()
