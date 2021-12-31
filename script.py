# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup
import sys
import json

#----------------------- VARIABLES -------------------------------------------------------------------
# Dictionnaire des prix (pays | prix en €)
prices = {
"fr": "",
"de":"",
"es":"",
"it":"",
"pl":"",
"nl":"",
}

# récupérer URL depuis argument du programme)
URL=sys.argv[1] if len(sys.argv) > 1 else print("Please give in argument amazon product link  to scrap. ") & quit()


#----------------------- FUNCTIONS  -------------------------------------------------------------------

# Trier les prix dans l'ordre croissant
def sort_prices(prices):
        prices = sorted(prices.items(), key=lambda x:x[1])
        prices = dict(prices)
        return prices

# Conserver uniquement le prix (sans le symbole devise)
def no_device(price):
        trim = re.compile(r'[^\d.,]+')
        result = trim.sub('', price)
        result = result.replace(",", ".")
        return result 

# Vérifier si la variable n'est pas vide
def checkamount(price):
        if ',' not in price:
                return "N/A"
        else:
                return price

# Récupérer le prix depuis Amazon

def get_title(domain_URL):
    page = requests.get(domain_URL,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"})
    soup = BeautifulSoup(page.content, "html.parser")
     
    try:
        title = soup.find("span",attrs={"id": 'productTitle'}).get_text(strip=True)
        #soup.find("span", {"class":"a-offscreen"}, {"class": "a-price a-text-price a-size-medium apexPriceToPay"}).get_text(strip=True)
                
        print("Product Title : " + title)
    except:
        pass


def get_price(domain_URL):

        page = requests.get(domain_URL,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"})
        soup = BeautifulSoup(page.content, "html.parser")
        price=""
        
        


        #récupérer le prix dans la page amaozn selon différente méthodes (différent cas de figure - class html)
        try:
                price = soup.find("span", {"class":"a-offscreen"}, {"class": "a-price a-text-price a-size-medium apexPriceToPay"}).get_text(strip=True)
                return price
                
        except:
                pass

        try:
                price = soup.find(id="priceblock_ourprice").get_text()
                return price
                
        except:
                pass

        try:
                price = soup.find("span", {"class":"a-offscreen"}, {"class": "a-price a-text-price header-price a-size-base a-text-normal"}).get_text(strip=True)
                return price
                
        except:
                return "N/A"
""""
        if price!= "":
                print(price)
"""



#----------------------- MAIN -------------------------------------------------------------------
get_title(URL)

for i in prices.keys():
        splitted_url = URL.split("/")
        
        for idx, val in enumerate(splitted_url):
            if val.startswith("www.amazon"):
                splitted_url[idx] = "www.amazon." + i
                caractere="/"
                final_url= caractere.join(splitted_url)
                
                try:
                        price = get_price(final_url)
                        price = no_device(price)
                        price = float(price)
                        
                except:
                        pass
                try:
                        price = float(price)
                        if i == "pl":
                                price = price*0.22
                except:
                        pass
                
                
                if price == "":
                        price = 0.0

                price = float(price)
                prices[i] = price # ajouer le prix courant dans le dictionnaire



prices = sort_prices(prices) # Trier les prix par ordre croissant

json_prices = json.dumps(prices, indent = 4, ensure_ascii=False) # Dictionnaire prices en format json
print(json_prices)


