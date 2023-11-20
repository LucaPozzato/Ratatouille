# Ratatouille

This project is the end result of an Hackathon. 

I was in a team of 5 people and we had 36 hours to present a product with the theme of well-being. Our team and I decide to create an app that follows the customer in the journey from buying groceries to having a meal. The app has 4 main features:

* First feature is to be able to compare the supermarkets and choose the cheapest one given a list of products (due to time restrictions we just compared two supermarkets: Carrefour and Penny) 

* Second feature of the app is to have a virtual fridge/pantry where the customer can see all the products that he has in the fridge/pantry, their shelf life and when it was opened

* Third feature is the management of the pantry/fridge
  * The first action is adding the products to the pantry, this can be done in three ways:
    * By manually by adding the product 
    * By uploading a picture of the product
    * By sending an audio where the customer says everything he bough at the supermaket
  * Second action is the deletion of products
  * Third action is setting the date when a certain product was opened (the customer when pressing the burron sets "today" as the day when it was opened)

* Forth feature is to generate a recipe based only on what the customer has in the fridge

I was responsible to the backend of the application and this repo is the end result of my work (special thanks to [Niccolò Puccia](https://github.com/niccolopuccia) who took care of the supermarket compare feature in [comparator.py](https://github.com/LucaPozzato/Ratatouille/blob/main/comparator.py)) 

## Server API

### List of products -> /pantry

GET request, returns a json file with all the items in database

> Request: \
`curl -i http://SERVER_IP:SERVER_PORT/pantry`

> Response: \
`{"pantry":[{"category":"Pasta","date":"2023-11-19","product":"Pasta","shelf_life":365},{"category":"Bananas","date":"n/a","product":"Banane","shelf_life":7}]}`

### Add product manually -> /pantry/add

POST requests, payload needs to be a json file (formatted as shown in example)

> Request: \
`curl -i http://SERVER_IP:SERVER_PORT/pantry/add -X POST -H 'Content-Type: application/json' -d '{"product": PRODUCT, "category": CATEGORY, "shelf_life": DAYS}'`

### Delete product -> /pantry/delete

POST request, payload needs to be a json file (formatted as shown in example)

> Request: \
`curl -i http://SERVER_IP:SERVER_PORT/pantry/delete -X POST -H 'Content-Type: application/json' -d '{"product": PRODUCT}'`

### Identify product via image -> /pantry/identify

POST request, payload needs to be a multipart image (formatted as shown in example). Response is a json file with the product

> Request: \
`curl -i http://SERVER_IP:SERVER_PORT/pantry/identify -X POST --form file='@image.png'`

> Response: \
`{"category":"Tomatoes","date":"n/a","product":"Redsun Cocktail Tomatoes","shelf_life":7}`

### Identify product via image -> /pantry/identify/json

POST request, payload needs to be a json file (formatted as shown in example), image needs to be encoded in base64. Response is a json file with the product

> Request: \
`curl -i http://SERVER_IP:SERVER_PORT/pantry/identify -X POST -H 'Content-Type: application/json' -d '{"image": ENCODED_IMAGE_BASE64}'`

> Response: same as /pantry/identify

### Add indentified product -> /pantry/identify/confirm

GET request (After you see identified product, if it's correct you add it like this)

> Request: \
`curl -i http://SERVER_IP:SERVER_PORT/pantry/identify/confirm`

### Cancel indentified product -> /pantry/identify/cancel

GET request (After you see identified product, if it's not correct you don't add it)

> Request: \
`curl -i http://SERVER_IP:SERVER_PORT/pantry/identify/cancel`

### Identify product via audio -> /pantry/audio

POST request, payload needs to be a multipart mp3 audio file (formatted as shown in example). Response is a json file with the product

> Request: \
`curl -i http://SERVER_IP:SERVER_PORT/pantry/identify -X POST --form file='@audio.mp3'`

> Response: \
`[{"category":"Pasta","date":"n/a","product":"Pasta","shelf_life":365},{"category":"Bananas","date":"n/a","product":"Banane","shelf_life":7}]`

### Identify product via audio -> /pantry/audio/json

POST request, payload needs to be a json file (formatted as shown in example), image needs to be encoded in base64. Response is a json file with the product

> Request: \
`curl -i http://SERVER_IP:SERVER_PORT/pantry/identify -X POST -H 'Content-Type: application/json' -d '{"audio": ENCODED_AUDIO_BASE64, "format": AUDIO_FILE_FORMAT}'`

> Response: same as /pantry/audio

### Add indentified product -> /pantry/audio/confirm

GET request (After you see identified products, if it's correct you add it like this)

> Request: \
`curl -i http://SERVER_IP:SERVER_PORT/pantry/audio/confirm`

### Cancel indentified product -> /pantry/audio/cancel

GET request (After you see identified products, if it's not correct you don't add it)

> Request: \
`curl -i http://SERVER_IP:SERVER_PORT/pantry/audio/cancel`

### Compare supermarkets -> /compare

POST request, payload needs to be a json file (formatted as shown in example, with products in a string separated by comma with no space). Response is a json with the supermarket and the total cost of the products (in €)

> Request: \
`curl -i http://SERVER_IP:SERVER_PORT/compare -X POST -H 'Content-Type: application/json' -d '{"list": "gocciole,pasta"}'`

> Response: \
`{"Carr_list":" -- Product: Pavesi Gocciole Wild Biscotti con Gocce di Cioccolato e Farina Integrale 350g, Price: 2.55 -- Product: Barilla Pasta Penne Rigate n.73 100% Grano Italiano 500g, Price: 1.25","Carrefour":"9.04","Penny":"8.34","Penny_list":" -- Product: Pavesi Gocciole Chocolate Biscotti con Gocce di Cioccolato 500g, Price: 2.99 -- Product: Percoche pasta gialla or. spa, Price: 0.29"}`

### Get recipe from products in database -> /recipe

GET request, returns a json file with the recipe

> Request: \
`curl -i http://SERVER_IP:SERVER_PORT/recipe`

> Response: \
`{"recipe": "Considering the ingredients given, you can make a simple \"Nutella Filled Croissant with Corn Cream Sauce\". Here's how:\n\nIngredients:\n- Croissant\n- Nutella\n- Pane morbido di grano duro (Optional, can also be replaced by normal bread)\n- Panna da cucina\n- Bonduelle Gold Zlat\u00e1 Kukurica (Canned corn)\n\nInstructions:\n\n1. Warm up your croissants at about 180 degrees in a preheated oven for about 5 minutes. \n\n2. Cut the croissants on one side to create a pocket.\n\n3. Fill the croissant with Nutella (use as much as you prefer).\n\n4. For the corn cream sauce, open up the can of Bonduelle Gold Zlat\u00e1 Kukurica / Canned corn and drain the water.\n\n5. Heat a pan. Add the canned corn and cook for about 3-5 minutes.\n\n6. Lower the heat, add Panna da cucina (heavy cream) to the corn and cook for another 2-3 minutes. Let the corn combination cool.\n\n7. Once cooled, start blending the corn and cream mix till it turns into a smooth paste.\n\n8. Drizzle your corn cream sauce on top of your Nutella filled croissants before serving.\n\nEnjoy your sweet and savoury treat!\n\nAs a note, the \"Pane morbido di grano duro - Esselunga - 400 g\" is a type of bread and the \"San Benedetto th\u00e8 Limone deteinato 0,5\" is a type of lemon tea. These ingredients don't quite fit into the suggested recipe and are hence, optional. On a side note, you can definitely enjoy the lemon tea as a refreshing drink with this sweet and savory treat."}`

### Set product as opened -> /date

POST request, payload needs to be a json file (formatted as shown in example)

> Request: \
`curl -i http://SERVER_IP:SERVER_PORT/pantry/date -X POST -H 'Content-Type: application/json' -d '{"product": PRODUCT}'`

## Run the server

### Install requirements

> pip install -r requirements.txt

### Run flask server

#### Set the API keys necessary for the server to work

OpenaAI key here -> [OpenAI site](https://platform.openai.com/docs/overview)\
Serpapi key here -> [Serpapi site](https://serpapi.com) \
IMGBB key here -> [IMGBB site](https://api.imgbb.com)

> export OPENAI_KEY=key

> export SERPAPI_KEY=key

> export IMGBB_KEY=key

#### Run server

> export FLASK_APP=server.py

> export FLASK_DEBUG=development

finally run the server

> flask run

or if you wanna use ip address of computer

> flask run -h 0.0.0.0 -p PORT