import csv
from db import Model, Session, engine
from models import Product,Manufacturer
from test import manufacturer_name


def main():
    Model.metadata.drop_all(engine)
    Model.metadata.create_all(engine)

    with Session() as session:
        with session.begin():
            with open('products.csv',encoding='utf8') as f:
                reader = csv.DictReader(f)

                for row in reader:
                    row['year'] = int(row['year'])

                    manufacturer_name = row.pop('manufacturer')

                    manufacturer = session.query(Manufacturer).filter(Manufacturer.name == manufacturer_name).first()

                    if manufacturer is None:
                        manufacturer = Manufacturer(name=manufacturer_name)
                        session.add(manufacturer)
                        session.flush()

                    row['manufacturer_id'] = manufacturer.id
                    product = Product(**row)
                    session.add(product)


if __name__ == '__main__':
    main()