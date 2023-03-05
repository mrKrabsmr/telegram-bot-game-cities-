from sqlalchemy import Table

from secret_data.db import meta, engine

cities = Table('cities', meta, autoload_with=engine)
