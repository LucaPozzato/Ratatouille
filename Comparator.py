from bs4 import BeautifulSoup
import requests
import re

def getTotal(list):
    global tot_carr
    global tot_pam

    for product in list:
        (tot_pam, tot_carr) = comparaProdotto(product)
    result_pam = "{:.2f}".format(tot_pam)
    result_carr = "{:.2f}".format(tot_carr)
    #print(result_pam)
    #print(result_carr)
    Dictionary = {}
    Dictionary['pam'] = result_pam
    Dictionary['carr'] = result_carr
    return Dictionary

def comparaProdotto(product):

    global tot_carr
    global tot_pam

    url = f"https://pamacasa.pampanorama.it/spesa-consegna-domicilio/20135/ricerca?search={product}&sort=asc"
    result = requests.get(url).text
    doc = BeautifulSoup(result, "html.parser")
    
    # print("########## PAM")


    name = doc.find_all(itemprop="name")
    name1 = name[1]
    name_str1 = str(name1).split('"')[-4]
    # print(name_str1)


    brand1 = doc.find(class_="brand-name").text
    # print(brand1.strip())

    price1 = doc.find(class_="price").text.strip()
    # print(price1)
    price_num1 = float(str(price1).split("€")[-2].replace(',','.'))
    # print("PRICE_NUM:", price_num1)

    tot_pam = tot_pam + price_num1


    #fine ricerca pam



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

   # print("\n\nBUY HERE: ")

    #if(price_num2<price_num1): 
     #  print("CARREFOUR")
    #else:
     # print("PAM")
    
    return (tot_pam, tot_carr)

#main

tot_pam = 0
tot_carr = 0