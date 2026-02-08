from flask import Flask, render_template, request
from parsers import read_json_products, read_csv_products

app = Flask(__name__)

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
