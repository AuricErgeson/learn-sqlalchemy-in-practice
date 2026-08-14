from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from models import Base

load_dotenv()

engine = create_engine(os.environ['DATABASE_URL'],echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(engine)