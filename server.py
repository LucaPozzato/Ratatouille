# server.py

from flask import Flask, request, jsonify
# import sqlite3
import identifier

app = Flask(__name__)

# con = sqlite3.connect("pantry.db")
# cur = con.cursor()

pantry = [
    {"product": "Croissant", "category": "Bakery", "shelf_life": "1-2 days"},
    {"product": "Nutella", "category": "Spread", "shelf_life": "1 year"}
]

id_product = ''

@app.get("/pantry")
def list_pantry():
    return jsonify(pantry)

@app.post("/pantry/add")
def get_product():
    if request.is_json:
        product = request.get_json()
        pantry.append(product)
        return product
    return {"error": "Request must be JSON"}, 415

@app.post("/pantry/delete")
def del_product():
    if request.is_json:
        product = request.get_json()
        product_name = product["product"]
        for i in pantry:
            if i["product"] == product_name:
                pantry.remove(i)
        return "OK", 200
    return {"error": "Request must be JSON"}, 415

@app.post("/pantry/identify")
def identify_product():
    if request.is_json:
        to_id = request.get_json()
        image = to_id["image"]
        id_product = identifier.get_product(image=image)
        # pantry.append(product)
        return jsonify(id_product)
    return {"error": "Request must be JSON"}, 415

@app.post("/pantry/identify/confirm")
def confirm():
    # add id_product to pantry
    return 0

@app.post("/compare")
def compare_product():
    if request.is_json:
        data = request.get_json()
        product = data["product"]
        return jsonify(product)
    return {"error": "Request must be JSON"}, 415

@app.get("/recipe")
def add_country():
    return jsonify(pantry)

