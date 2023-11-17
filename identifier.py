import requests
import json
from serpapi import GoogleSearch

IMGBB_KEY = 'badf49d65ddf6637dc8fd30bb31e1c52'
IMGBB_URL = 'https://api.imgbb.com/1/upload?expiration=60&key='+IMGBB_KEY

SERPAPI_KEY = '39fe1beb8879e1e647624a3c1e0fc836a936bafc392aa6c1c08ff27fd25f7d87'

# CHATGPT_KEY = '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'

true = True

def get_product(image):
    url = upload(image=image)
    product = product_name(url=url)
    return product

def upload(image):
    r = requests.post(IMGBB_URL, data={'image': image})
    response = r.text
    dict = json.loads(response)
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

with open('base64_img.txt', 'r') as file:
    base64_img = file.read().rstrip()