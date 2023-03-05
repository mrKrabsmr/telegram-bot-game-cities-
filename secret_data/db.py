from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import create_session, declarative_base

engine = create_engine('postgresql://postgres:V7CyStMHLiFsXbrBXkRY@containers-us-west-44.railway.app:6439/railway')
meta = MetaData()
Base = declarative_base()


session = create_session(engine)
