from sqlalchemy import create_engine,text
from dotenv import load_dotenv
import os


load_dotenv()

engine = create_engine(os.environ['DATABASE_URL'],echo=True)

"""with engine.connect() as connection:
    result = connection.execute(text('select "Hello"'))
    print(result.all())"""

