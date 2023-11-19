from bs4 import BeautifulSoup
import requests

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

    # print(result_pam)
    # print(result_carr)

    Dictionary = {}
    Dictionary['Penny'] = result_pam
    Dictionary['Carrefour'] = result_carr
    Dictionary['Penny_list'] = pam_list
    Dictionary['Carr_list'] = carr_list
    
    print(Dictionary)
    return Dictionary

def comparaProdotto(product):
    global tot_carr
    global tot_conad

    url = f"https://www.carrefour.it/search?q={product}&srule=price-low-to-high"
    result = requests.get(url).text
    doc = BeautifulSoup(result, "html.parser")
    
    # print("\n\n########## CARREFOUR")

    name2 = doc.find(class_="tile-description").text.strip()
    # print(name2)

    brand2 = doc.find(class_="brand").text.strip()
    # print(brand2)

    price2 = doc.find(class_="value").text.strip()
    # print(price2)
    price_num2 = float(str(price2).split("€")[-1].split(" ")[-1].replace(',','.'))
    # print("PRICE_NUM:", price_num2)

    tot_carr = tot_carr + price_num2
    product_carr = "Product: " + str(name2) + ", " + "Price: " + str(price_num2)

    # print(product_carr)

    url = f"https://pennyacasa.it/ricerca?search={product}&sort=asc"
    result = requests.get(url).text
    doc = BeautifulSoup(result, "html.parser")
    
    # print("########## PENNY")

    name = doc.find_all(itemprop="name")
    name1 = name[3]
    name_str1 = str(name1).split('=')[-2]
    name_str2 = str(name_str1).split('"')[-2]
    # print(name_str2)

    brand1 = "Conad"
    # print(brand1)

    price1 = doc.find(class_="price").text.strip()
    # print(price1)
    price_num1 = float(str(price1).split(" ")[-2].replace(',','.'))
    # print(price_num1)
    

    tot_conad = tot_conad + price_num1

    product_pam = "Product: " + name_str2 + ", " + "Price: " + str(price_num1)
    #fine ricerca pam

    # print("\n\nBUY HERE: ")

    # if(price_num2<price_num1): 
    #   print("CARREFOUR")
    # else:
    #  print("PAM")
    
    return (product_pam, product_carr)

#main
tot_conad = 0
tot_carr = 0

# products = "salsa,pomodoro,miele"

# getTotal(products.split(","))