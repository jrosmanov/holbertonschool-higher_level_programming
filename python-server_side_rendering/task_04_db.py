from flask import Flask, render_template, request
from parsers import read_csv_products, read_json_products, read_database

app = Flask(__name__)

@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source not in ("json", "csv", "sql"):
        return render_template(
            "product_display.html",
            error="Wrong source",
            products=[]
        )

    try:
        if source == "json":
            products = read_json_products()
        elif source == 'csv':
            products = read_csv_products()
        else:
            products = read_database()
    except Exception:
        return render_template(
            "product_display.html",
            error="Error reading data file",
            products=[]
        )

    # Filter by id if provided
    if product_id is not None:
        try:
            product_id = int(product_id)
            products = [p for p in products if p["id"] == product_id]
            if not products:
                return render_template(
                    "product_display.html",
                    error="Product not found",
                    products=[]
                )
        except ValueError:
            return render_template(
                "product_display.html",
                error="Invalid product id",
                products=[]
            )

    return render_template(
        "product_display.html",
        products=products,
        error=None
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)