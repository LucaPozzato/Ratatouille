# server.py

from flask import Flask, request, jsonify
import sqlite3
import identifier
import recipe
import comparator
import f_audio
import json
import ast
import os

app = Flask(__name__)

id_product = ''
id_dict = ''

@app.get("/pantry")
def list_pantry():
    conn = sqlite3.connect('pantry.db')
    cursor = conn.cursor()

    select_all_query = '''
    SELECT product, category, shelf_life
    FROM products;
    '''
    cursor.execute(select_all_query)

    products_data = cursor.fetchall()

    products_dict_list = []
    for product_data in products_data:
        product_dict = {
            'product': product_data[0],
            'category': product_data[1],
            'shelf_life': product_data[2],
            'date': product_data[3]
        }
        products_dict_list.append(product_dict)

    pantry_dict = {}
    pantry_dict["pantry"] = products_dict_list

    conn.close()
    return jsonify(pantry_dict), 200

@app.post("/pantry/add")
def get_product():
    if request.is_json:
        conn = sqlite3.connect('pantry.db')
        cursor = conn.cursor()

        json_data = request.get_json()

        new_product = json_data['product']
        new_category = json_data['category']
        new_shelf_life = json_data['shelf_life']
        new_date = json_data['date']

        get_max_id_query = '''
        SELECT MAX(id) FROM products;
        '''

        cursor.execute(get_max_id_query)
        max_id = cursor.fetchone()[0]
        new_id = max_id + 1 if max_id is not None else 1

        insert_new_product_query = f'''
        INSERT INTO products (id, product, category, shelf_life, date)
        VALUES ({new_id}, '{new_product}', '{new_category}', {new_shelf_life}, '{new_date}');
        '''

        cursor.execute(insert_new_product_query)

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

        delete_product_query = f'''
        DELETE FROM products
        WHERE product = '{product_to_delete}';
        '''
        cursor.execute(delete_product_query)

        conn.commit()
        conn.close()

        return "OK", 200
    return {"error": "Request must be JSON"}, 415

@app.post("/pantry/identify")
def identify_product():
    if request.is_json:
        to_id = request.get_json()
        image = to_id["image"]

        os.system("rm image.txt")

        f = open("image.txt", "w")
        f.write(image)
        f.close()

        global id_product

        id_product = identifier.get_product()
        product_dict = json.loads(id_product)
        return jsonify(product_dict), 200
    return {"error": "Request must be JSON"}, 415

@app.get("/pantry/identify/confirm")
def img_confirm():
    conn = sqlite3.connect('pantry.db')
    cursor = conn.cursor()

    global id_product

    json_data = json.loads(id_product)
    # print(json_data)

    new_product = json_data['product']
    new_category = json_data['category']
    new_shelf_life = json_data['shelf_life']
    new_date = json_data['date']

    get_max_id_query = '''
    SELECT MAX(id) FROM products;
    '''

    cursor.execute(get_max_id_query)
    max_id = cursor.fetchone()[0]
    new_id = max_id + 1 if max_id is not None else 1

    insert_new_product_query = f'''
    INSERT INTO products (id, product, category, shelf_life, date)
    VALUES ({new_id}, '{new_product}', '{new_category}', {new_shelf_life}, '{new_date}');
    '''

    cursor.execute(insert_new_product_query)

    conn.commit()
    conn.close()

    id_product = ''
    return "OK", 200

@app.get("/pantry/identify/cancel")
def img_cancel():
    global id_product
    id_product = ''
    return "OK", 200

@app.post("/compare")
def compare_product():
    if request.is_json:
        data = request.get_json()
        products = data["list"]
        result = comparator.getTotal(products)
        return jsonify(result), 200
    return {"error": "Request must be JSON"}, 415

@app.get("/recipe")
def add_country():
    conn = sqlite3.connect('pantry.db')
    cursor = conn.cursor()

    select_product_names_query = '''
    SELECT product
    FROM products;
    '''

    cursor.execute(select_product_names_query)

    product_names = cursor.fetchall()

    product_names_list = [product[0] for product in product_names]
    conn.close()

    response = recipe.recipe_gen(product_names_list)

    recipe_dict = {}
    recipe_dict["recipe"] = response

    return jsonify(recipe_dict), 200

@app.post("/pantry/audio")
def insert_audio():
    if request.is_json:
        to_aud = request.get_json()
        audio = to_aud["audio"]
        format = to_aud["format"]

        os.system("rm audio.txt")

        f = open("audio.txt", "w")
        f.write(audio)
        f.close()

        transcript = f_audio.get_audio(format)
        
        global id_dict
        id_dict = transcript

        return jsonify(transcript), 200
    return {"error": "Request must be JSON"}, 415

@app.get("/pantry/audio/confirm")
def audio_confirm():
    conn = sqlite3.connect('pantry.db')
    cursor = conn.cursor()

    global id_dict

    json_data = ast.literal_eval(id_dict)

    for i in json_data:
        new_product = i['product']
        new_category = i['category']
        new_shelf_life = i['shelf_life']
        new_date = i['date']

        get_max_id_query = '''
        SELECT MAX(id) FROM products;
        '''

        cursor.execute(get_max_id_query)
        max_id = cursor.fetchone()[0]
        new_id = max_id + 1 if max_id is not None else 1

        insert_new_product_query = f'''
        INSERT INTO products (id, product, category, shelf_life, date)
        VALUES ({new_id}, '{new_product}', '{new_category}', {new_shelf_life}, '{new_date}');
        '''

        cursor.execute(insert_new_product_query)

    conn.commit()
    conn.close()

    id_dict = ''
    return "OK", 200

@app.get("/pantry/audio/cancel")
def audio_cancel():
    global id_dict
    id_dict = ''
    return "OK", 200
