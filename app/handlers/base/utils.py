from random import choice

from app.container import city_service, user_service


def between_func(message):
    lst = []
    for row in city_service.get_by_last_letter(message).all():
        lst.append(row[-1])
    if len(lst) == 0:
        return False
    return lst


def game_func_one(message):
    if not between_func(message):
        return False
    while True:
        city = choice(between_func(message))
        if city[-1] not in 'ъыь':
            return city


def game_func_two(message):
    lst = []
    for row in city_service.get_all().all():
        lst.append(row[-1].capitalize())

    return message.capitalize() in lst


def game_func_three():
    while True:
        city = choice(city_service.get_all().all())
        if city[-1][-1] not in 'ъыь':
            return city


def game_func_four(username):
    user = user_service.get_one(username)
    cg = user.count_games + 1
    cw = user.count_wins + 1
    data = {
        "count_games": cg,
        "count_wins": cw
    }
    user_service.partial_update(user, data)


def game_func_five(username):
    user = user_service.get_one(username)
    cg = user.count_games + 1
    data = {
        "count_games": cg
    }
    user_service.partial_update(user, data)
