from app.container import user_service


def add_new_user_to_db(username):
    lst = []
    for user in user_service.get_all():
        lst.append(user.username)
    if username not in lst:
        data = {
            'username': username
        }
        user_service.create(data)


def my_profile_txt(message):
    if message.from_user.username is not None:
        user = user_service.get_one(message.from_user.username)
    else:
        user = user_service.get_one(message.from_user.full_name)
    return f"""
Имя:    <em>{message.from_user.full_name}</em>
username:    <em>{user.username}</em>
Количество игр:    <em>{user.count_games}</em>
Количество побед:    <em>{user.count_wins}</em>
"""


def top_users_txt():
    text = ''
    n = 1
    for user in user_service.get_top_users():
        text += f"{n}. @{user.username}   победы: {user.count_wins}   игры: {user.count_games}\n"
        n += 1
    return text
