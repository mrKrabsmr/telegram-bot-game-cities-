from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import create_session, declarative_base

engine = create_engine('postgresql://postgres:17631864-Perec@localhost:5432/bot')
meta = MetaData()
Base = declarative_base()


session = create_session(engine)
