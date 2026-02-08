import json, csv
import db

def read_json_products():
    with open("products.json", "r") as f:
        return json.load(f)

def read_csv_products():
    products = []
    with open("products.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

def read_database():
    list_of_tables = ['id', 'name', 'category', 'price']
    data = db.show()
    products = []

    for tup in data:
        product_sample = {}
        for index, i in enumerate(list_of_tables):
            product_sample[i] = tup[index]
        products.append(product_sample)

    return products

read_database()