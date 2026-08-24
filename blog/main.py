from sqlalchemy.orm import Session
from connect import engine


Session = Session(bind=engine)
