from app.database.dao.city import CityDAO
from app.database.dao.models.city import cities
from app.database.dao.user import UserDAO
from app.database.services.city import CityService
from app.database.services.user import UserService
from secret_data.db import engine, session

city_dao = CityDAO(conn=engine.connect(), cities=cities)
city_service = CityService(dao=city_dao)

user_dao = UserDAO(session)
user_service = UserService(user_dao)