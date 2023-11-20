from bs4 import BeautifulSoup
import requests

tot_conad = 0
tot_carr = 0

def getTotal(list):
    global tot_carr
    global tot_conad

    pam_list = ''
    carr_list = ''

    for product in list:
        (product_pam, product_carr) = comparaProdotto(product)
        pam_list = pam_list + " -- " + product_pam
        carr_list = carr_list + " -- " + product_carr

    result_pam = "{:.2f}".format(tot_conad)
    result_carr = "{:.2f}".format(tot_carr)

    Dictionary = {}
    Dictionary['Penny'] = result_pam
    Dictionary['Carrefour'] = result_carr
    Dictionary['Penny_list'] = pam_list
    Dictionary['Carr_list'] = carr_list
    
    return Dictionary

def comparaProdotto(product):
    global tot_carr
    global tot_conad

    url = f"https://www.carrefour.it/search?q={product}&srule=price-low-to-high"
    result = requests.get(url).text
    doc = BeautifulSoup(result, "html.parser")

    name2 = doc.find(class_="tile-description").text.strip()
    brand2 = doc.find(class_="brand").text.strip()
    price2 = doc.find(class_="value").text.strip()

    price_num2 = float(str(price2).split("€")[-1].split(" ")[-1].replace(',','.'))

    tot_carr = tot_carr + price_num2
    product_carr = "Product: " + str(name2) + ", " + "Price: " + str(price_num2)

    url = f"https://pennyacasa.it/ricerca?search={product}&sort=asc"
    result = requests.get(url).text
    doc = BeautifulSoup(result, "html.parser")

    name = doc.find_all(itemprop="name")
    name1 = name[3]
    name_str1 = str(name1).split('=')[-2]
    name_str2 = str(name_str1).split('"')[-2]
    brand1 = "Conad"
    price1 = doc.find(class_="price").text.strip()

    price_num1 = float(str(price1).split(" ")[-2].replace(',','.'))

    tot_conad = tot_conad + price_num1

    product_pam = "Product: " + name_str2 + ", " + "Price: " + str(price_num1)

    return (product_pam, product_carr)