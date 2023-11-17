# server.py

from flask import Flask, request, jsonify
import sqlite3
import identifier
import recipe
import Comparator
import json

app = Flask(__name__)

id_product = ''

@app.get("/pantry")
def list_pantry():
    conn = sqlite3.connect('pantry.db')
    cursor = conn.cursor()

    select_all_query = '''
    SELECT product, category, shelf_life
    FROM products;
    '''

    # Execute the query
    cursor.execute(select_all_query)

    # Fetch all the results
    products_data = cursor.fetchall()

    # Organize the results into a dictionary
    products_dict_list = []
    for product_data in products_data:
        product_dict = {
            'product': product_data[0],
            'category': product_data[1],
            'shelf_life': product_data[2]
        }
        products_dict_list.append(product_dict)

    conn.close()
    return jsonify(products_dict_list)

@app.post("/pantry/add")
def get_product():
    if request.is_json:
        conn = sqlite3.connect('pantry.db')
        cursor = conn.cursor()

        json_data = request.get_json()

        # Extract product, category, and shelf_life from the JSON data
        new_product = json_data['product']
        new_category = json_data['category']
        new_shelf_life = json_data['shelf_life']

        # Determine the new id by finding the maximum existing id and adding 1
        get_max_id_query = '''
        SELECT MAX(id) FROM products;
        '''

        cursor.execute(get_max_id_query)
        max_id = cursor.fetchone()[0]
        new_id = max_id + 1 if max_id is not None else 1

        # Insert the new product data into the database
        insert_new_product_query = f'''
        INSERT INTO products (id, product, category, shelf_life)
        VALUES ({new_id}, '{new_product}', '{new_category}', {new_shelf_life});
        '''

        cursor.execute(insert_new_product_query)

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        return "OK", 200
    return {"error": "Request must be JSON"}, 415

@app.post("/pantry/delete")
def del_product():
    if request.is_json:
        conn = sqlite3.connect('pantry.db')
        cursor = conn.cursor()

        product = request.get_json()

        product_to_delete = product["product"]

        # Delete the product by name
        delete_product_query = f'''
        DELETE FROM products
        WHERE product = '{product_to_delete}';
        '''

        # Execute the query
        cursor.execute(delete_product_query)

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        return "OK", 200
    return {"error": "Request must be JSON"}, 415

@app.post("/pantry/identify")
def identify_product():
    if request.is_json:
        to_id = request.get_json()
        image = to_id["image"]
        global id_product
        id_product = identifier.get_product(image=image)
        return jsonify(id_product)
    return {"error": "Request must be JSON"}, 415

@app.get("/pantry/identify/confirm")
def confirm():
    conn = sqlite3.connect('pantry.db')
    cursor = conn.cursor()

    global id_product

    json_data = json.loads(id_product)
    print(json_data)

    # Extract product, category, and shelf_life from the JSON data
    new_product = json_data['product']
    new_category = json_data['category']
    new_shelf_life = json_data['shelf_life']

    # Determine the new id by finding the maximum existing id and adding 1
    get_max_id_query = '''
    SELECT MAX(id) FROM products;
    '''

    cursor.execute(get_max_id_query)
    max_id = cursor.fetchone()[0]
    new_id = max_id + 1 if max_id is not None else 1

    # Insert the new product data into the database
    insert_new_product_query = f'''
    INSERT INTO products (id, product, category, shelf_life)
    VALUES ({new_id}, '{new_product}', '{new_category}', {new_shelf_life});
    '''

    cursor.execute(insert_new_product_query)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    id_product = ''
    return "OK", 200

@app.get("/pantry/identify/cancel")
def cancel():
    global id_product
    id_product = ''
    return "OK", 200

@app.post("/compare")
def compare_product():
    if request.is_json:
        data = request.get_json()
        product = data["list"]
        return jsonify(product)
    return {"error": "Request must be JSON"}, 415

@app.get("/recipe")
def add_country():
    conn = sqlite3.connect('pantry.db')
    cursor = conn.cursor()

    # Execute a query to retrieve all product names from the products table
    select_product_names_query = '''
    SELECT product
    FROM products;
    '''

    # Execute the query
    cursor.execute(select_product_names_query)

    # Fetch all the results
    product_names = cursor.fetchall()

    # Organize the results into a list
    product_names_list = [product[0] for product in product_names]
    conn.close()

    response = recipe.recipe_gen(product_names_list)

    return jsonify(response), 200

