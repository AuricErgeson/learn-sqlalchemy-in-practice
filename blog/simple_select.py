from main import Session
from models import User


users = Session.query(User).all()

for user in users:
    print(user)
