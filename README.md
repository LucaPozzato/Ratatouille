# Ratatouille

## Server API

### List of products -> /pantry

GET request, returns a json file with all the items in database

> Request: \
`curl -i http://SERVER_IP:SERVER_PORT/pantry`

> Response: \
`[
  { 
    "category": "Bakery",
    "product": "Croissant",
    "shelf_life": 2
  },
  {
    "category": "Spread",
    "product": "Nutella",
    "shelf_life": 365
  }
]`

### Add product manually -> /pantry/add

POST requests, payload needs to be a json file (formatted as shown in example)

> Request: \
`curl -i http://SERVER_IP:SERVER_PORT/pantry/add -X POST -H 'Content-Type: application/json' -d '{"product": PRODUCT, "category": CATEGORY, "shelf_life": DAYS}'`

### Delete product -> /pantry/delete

POST request, payload needs to be a json file (formatted as shown in example)

> Request: \
`curl -i http://SERVER_IP:SERVER_PORT/pantry/delete -X POST -H 'Content-Type: application/json' -d '{"product": PRODUCT}'`

### Identify product via image -> /pantry/identify

POST request, payload needs to be a json file (formatted as shown in example), image needs to be encoded in base64. Response is a json file with the product

> Request: \
`curl -i http://SERVER_IP:SERVER_PORT/pantry/identify -X POST -H 'Content-Type: application/json' -d '{"image": ENCODED_IMAGE_BASE64}'`

> Response: \
`{
  "category": "Tomatoes",
  "product": "Redsun Cocktail Tomatoes",
  "shelf_life": 7
}`

### Add indentified product -> /pantry/identify/confirm

GET request (After you see identified product, if it's correct you add it like this)

> Request: \
`curl -i http://SERVER_IP:SERVER_PORT/pantry/identify/add`

### Cancel indentified product -> /pantry/identify/cancel

GET request (After you see identified product, if it's not correct you don't add it)

> Request: \
`curl -i http://SERVER_IP:SERVER_PORT/pantry/identify/cancel`

### Compare supermarkets -> /compare

POST request, payload needs to be a json file (formatted as shown in example). Response is a json with the supermarket and the total cost of the products (in €)

> Request: \
`curl -i http://SERVER_IP:SERVER_PORT/compare -X POST -H 'Content-Type: application/json' -d '{"list": ["gocciole", "pasta", "pesto", "fagioli"]}'`

> Response: \
`{
  "Carrefour": "5.24",
  "Pam": "4.80"
}`

### Get recipe from products in database -> /recipe

GET request, returns a json file with the recipe

> Request: \
`curl -i http://SERVER_IP:SERVER_PORT/recipe`

> Response: \
`{
  "recipe": "Considering the ingredients given, you can make a simple \"Nutella Filled Croissant with Corn Cream Sauce\". Here's how:\n\nIngredients:\n- Croissant\n- Nutella\n- Pane morbido di grano duro (Optional, can also be replaced by normal bread)\n- Panna da cucina\n- Bonduelle Gold Zlat\u00e1 Kukurica (Canned corn)\n\nInstructions:\n\n1. Warm up your croissants at about 180 degrees in a preheated oven for about 5 minutes. \n\n2. Cut the croissants on one side to create a pocket.\n\n3. Fill the croissant with Nutella (use as much as you prefer).\n\n4. For the corn cream sauce, open up the can of Bonduelle Gold Zlat\u00e1 Kukurica / Canned corn and drain the water.\n\n5. Heat a pan. Add the canned corn and cook for about 3-5 minutes.\n\n6. Lower the heat, add Panna da cucina (heavy cream) to the corn and cook for another 2-3 minutes. Let the corn combination cool.\n\n7. Once cooled, start blending the corn and cream mix till it turns into a smooth paste.\n\n8. Drizzle your corn cream sauce on top of your Nutella filled croissants before serving.\n\nEnjoy your sweet and savoury treat!\n\nAs a note, the \"Pane morbido di grano duro - Esselunga - 400 g\" is a type of bread and the \"San Benedetto th\u00e8 Limone deteinato 0,5\" is a type of lemon tea. These ingredients don't quite fit into the suggested recipe and are hence, optional. On a side note, you can definitely enjoy the lemon tea as a refreshing drink with this sweet and savory treat."
}`

## Run the server

### Install requirements

> pip install -r requirements.txt

### Run flask server

> export FLASK_APP=server.py

> export FLASK_DEBUG=development

#### Run server

> flask run

or if you wanna set use ip address of computer

> flask run -h 0.0.0.0 -p PORT
