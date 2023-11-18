import requests
import json
from serpapi import GoogleSearch
import openai

IMGBB_KEY = '2ca4ab41ed9360b631237197bbb7db6d'
IMGBB_URL = 'https://api.imgbb.com/1/upload?expiration=60&key='+IMGBB_KEY

SERPAPI_KEY = '39fe1beb8879e1e647624a3c1e0fc836a936bafc392aa6c1c08ff27fd25f7d87'

CHATGPT_KEY = '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'

true = True

def get_product():
    f = open("image.txt", "r")
    image = f.read()

    url = upload(image=image)
    product = product_name(url=url)
    product_dict = dict_gen(product)
    # print(product_dict)
    # print(type(product_dict))
    return product_dict

def upload(image):
    r = requests.post(IMGBB_URL, data={'image': image})
    response = r.text
    dict = json.loads(response)
    # print(dict)
    data = dict["data"]
    IMAGE_URL = data["url"]
    return IMAGE_URL

def product_name(url):
    params = {
    "engine": "google_lens",
    "url": url,
    "api_key": SERPAPI_KEY
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    if 'knowledge_graph' in results:
        return results['knowledge_graph'][0]['title']
    else:
        return results['visual_matches'][0]['title']

def dict_gen(product):
    client = openai.OpenAI(
        api_key=CHATGPT_KEY,
        # organization='org-oXnNlV1Z1fhmOWvYF8N6mjj2'
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "I need a dict that has a product, its product catgeory and the shelf_life which is an estimate of the expiration date. The dictionary should only have as keys: product, category in english, shelf_life is the string formatted like DD-MM-YYYY"},
            {"role": "user", "content": "the product is" + product}
        ]
    )
    return completion.choices[0].message.content
