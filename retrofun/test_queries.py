from models import Product
from db import  Session
from sqlalchemy import select


session = Session()

"""query_1 = select(Product)
result = session.execute(query_1)

for row in result:
    print(row)"""

query_1 = select(Product)
result = session.scalars(query_1)

for row in result:
    print(row)

