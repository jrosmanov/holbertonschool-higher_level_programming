from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

# ---------- JSON ----------
def read_json_products():
    with open("products.json", "r", encoding="utf-8") as f:
        return json.load(f)

# ---------- CSV ----------
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

# ---------- SQLITE ----------
def init_db():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM Products")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.executemany("""
            INSERT INTO Products (id, name, category, price)
            VALUES (?, ?, ?, ?)
        """, [
            (1, "Laptop", "Electronics", 799.99),
            (2, "Coffee Mug", "Home Goods", 15.99)
        ])

    conn.commit()
    conn.close()

def read_sql_products():
    init_db()
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()

    conn.close()

    return [
        {"id": r[0], "name": r[1], "category": r[2], "price": r[3]}
        for r in rows
    ]

# ---------- ROUTE ----------
@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source == "json":
        data = read_json_products()
    elif source == "csv":
        data = read_csv_products()
    elif source == "sql":
        data = read_sql_products()
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
