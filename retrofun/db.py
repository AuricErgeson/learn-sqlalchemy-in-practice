import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,sessionmaker

class Model(DeclarativeBase):
    pass

load_dotenv()

engine = create_engine(os.environ["DATABASE_URL"], echo=True)
Session = sessionmaker(bind=engine)

