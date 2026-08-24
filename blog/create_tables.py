from models import Base
from connect import engine

print("CREATING TABLES >>>> ")

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)