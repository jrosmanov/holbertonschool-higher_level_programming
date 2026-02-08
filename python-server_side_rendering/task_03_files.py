from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

def read_json_products():
    with open("products.json", "r", encoding="utf-8") as f:
        return json.load(f)

def read_csv_products():
    products = []
    if not os.path.exists("products.csv"):
        return products

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


@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source == "json":
        data = read_json_products()
    elif source == "csv":
        data = read_csv_products()
    else:
        return render_template(
            "product_display.html",
            error="Wrong source"
        )

    if product_id:
        product_id = int(product_id)
        data = [p for p in data if p["id"] == product_id]
        if not data:
            return render_template(
                "product_display.html",
                error="Product not found"
            )

    return render_template(
        "product_display.html",
        products=data
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)