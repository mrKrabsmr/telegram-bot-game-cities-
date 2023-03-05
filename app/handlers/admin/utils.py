from app.container import city_service, user_service


def check_is_admin(potential_admin):
    if potential_admin.username is None:
        user = user_service.get_one(potential_admin.full_name)
    else:
        user = user_service.get_one(potential_admin.username)
    if user.role in ('admin', 'superuser'):
        return True
    else:
        return False


def check_is_in_db(message):
    lst = []
    for row in city_service.get_all().all():
        lst.append(row[-1].capitalize())

    return message.capitalize() in lst
