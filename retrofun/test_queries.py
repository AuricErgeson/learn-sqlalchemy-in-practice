from models import Product
from db import  Session
from sqlalchemy import select, or_, func


session = Session()

query_1 = select(Product).where(Product.manufacturer == 'Commodore')

query_2 = (select(Product)
           .where(Product.manufacturer == 'Commodore')
           .where(Product.year == 1980))

query_3 = select(Product).where(or_(Product.year < 1970, Product.year > 1990))

query_4 = select(Product).where(Product.name.like('%Sinclair%'))

query_5 = select(func.count(Product.id))

query_6 = select(Product.manufacturer).order_by(Product.manufacturer).distinct()

query_7 =(
    select(
        Product.manufacturer,
        func.min(Product.year),
        func.max(Product.year),
        func.count()
    )
    .group_by(Product.manufacturer)
    .order_by(Product.manufacturer)
)

query_8 = (
    select(Product.country,
           func.min(Product.year),
           func.max(Product.year),
           func.count())
    .group_by(Product.country)
    .having(Product.country == 'Croatia')
)


result = session.scalar(query_5)
results = session.execute(query_8).all()

p = session.get(Product,170)

print(results)






