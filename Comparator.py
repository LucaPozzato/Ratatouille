from bs4 import BeautifulSoup
import requests
import re


product = input("Choose a product to compare: ")
#Andiamo a chiedere all'utente quale prodotto desidera cercare
#Apro la pagina dell'esselunga online per quel prodotto

url = f"https://pamacasa.pampanorama.it/spesa-consegna-domicilio/20135/ricerca?search={product}&sort=asc"

#Per visualizzare il contenuto html della pagina devo mandare una richiesta http che mi torna la pagina html
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")
#Ora posso visualizzare il contenuto della pagina html
 
print("########## PAM")


name = doc.find_all(itemprop="name")
name1 = name[1]
name_str1 = str(name1).split('"')[-4]
print(name_str1)


brand1 = doc.find(class_="brand-name").text
print(brand1.strip())

price1 = doc.find(class_="price").text.strip()
print(price1)
price_num1 = str(price1).split("€")[-2]
print("PRICE_NUM:", price_num1)



#Non permette di non essere soddisfatto dei prodotti che ti propongo 
#fine ricerca pam



url = f"https://www.carrefour.it/search?q={product}&srule=price-low-to-high"

result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")
 
print("\n\n########## CARREFOUR")


name2 = doc.find(class_="tile-description").text.strip()
print(name2)

brand2 = doc.find(class_="brand").text.strip()
print(brand2)

price2 = doc.find(class_="value").text.strip()
print(price2)
price_num2 = str(price2).split("€")[-1].split(" ")[-1]
print("PRICE_NUM:", price_num2)


print("\n\nBUY HERE: ")

if(price_num2<price_num1): 
    print("CARREFOUR")
else:
    print("PAM")