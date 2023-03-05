class UserService:
    def __init__(self, dao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, username):
        return self.dao.get_one(username)

    def get_top_users(self):
        return self.dao.get_top_users()

    def create(self, data):
        return self.dao.create(data)

    def update(self, user, new_data):
        user.username = new_data.get('username')
        user.count_games = new_data.get('count_games', 0)
        user.count_wins = new_data.get('count_wins', 0)
        user.best_time = new_data.get('best_time', None)
        return self.dao.update(user)

    def partial_update(self, user, new_data):
        if 'username' in new_data:
            user.username = new_data.get('username')
        if 'count_games' in new_data:
            user.count_games = new_data.get('count_games', 0)
        if 'count_wins' in new_data:
            user.count_wins = new_data.get('count_wins', 0)
        if 'best_time' in new_data:
            user.best_time = new_data.get('best_time', None)
        return self.dao.update(user)

    def delete(self, username):
        return self.dao.delete(username)

