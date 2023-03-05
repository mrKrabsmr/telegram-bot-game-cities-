from sqlalchemy import Column, Integer, String

from secret_data.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, index=True)
    count_games = Column(Integer, default=0)
    count_wins = Column(Integer, default=0)
    role = Column(String)
