from models import User, Comment
from main import Session

user1 = User(
    username="jona",
    email_address='jonathan@sql.irg',
    comments= [
        Comment(text='Hello World'),
        Comment(text='Please subscribe'),
    ]
)
user2 = User(
        username="paul",
        email_address='paul@sql.irg',
         comments=[
            Comment(text="What's up"),
            Comment(text='Please subscribe'),
    ]

)

cathy = User(
    username="cathy",
    email_address="cathy@sql.irg"
)

with Session as session:
    session.add(user1)
    session.add(user2)
    session.add(cathy)

    session.commit()
