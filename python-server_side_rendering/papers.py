import json
import csv

def read_json_products():
    with open("products.json", "r", encoding="utf-8") as f:
        return json.load(f)

def read_csv_products():
    products = []
    with open("products.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products
