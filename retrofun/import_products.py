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
                        #session.commit()

                    #row['manufacturer_id'] = manufacturer.id
                    manufacturer_id = session.query(Product.id).filter(
                        Product.manufacturer_id == manufacturer.id,
                        Product.name == row['name']
                    ).first()
                    if manufacturer_id is None:

                        product = Product(
                            name = row['name'],
                            manufacturer_id = manufacturer.id,
                            year = row['year'],
                            country = row['country'],
                            cpu=row['cpu'],

                        )
                        session.add(product)
                    #session.commit()


if __name__ == '__main__':
    main()