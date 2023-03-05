from app.database.dao.models.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(User).all()

    def get_one(self, username):
        return self.session.query(User).filter(User.username == username).one()

    def get_top_users(self):
        return self.session.query(User).order_by(User.count_wins.desc()).order_by(User.count_games.desc()).limit(
            10).all()

    def create(self, data):
        user = User(**data)
        self.session.add(user)
        self.session.commit()

    def update(self, user):
        self.session.add(user)
        self.session.commit()

    def delete(self, username):
        self.session.query(User).filter(User.username == username).delete()
        self.session.commit()
