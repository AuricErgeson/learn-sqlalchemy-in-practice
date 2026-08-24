from main import Session
from models import User

jona = Session.query(User).filter_by(
    username = 'jona'
).first()

print(jona)