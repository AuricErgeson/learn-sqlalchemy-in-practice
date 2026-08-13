import csv

with open("products.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        manufacturer_name = row.pop('manufacturer')
        print(manufacturer_name)


