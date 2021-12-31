from requests.api import request
from flask import Flask, render_template, jsonify, request
import os
import subprocess
import re
import requests
from bs4 import BeautifulSoup
import sys
import json 

app = Flask(__name__)
price = 0.0

@app.route('/')
def accueil():
    return '''<h1>Welcome to Amazon Best Prices (EU)</h1>'''

@app.route('/amazonbestprice', methods=['GET'])
def base():
     
    # récupérer URL depuis argument de la requete API
    URL = request.args.get('url')

    
    #----------------------- VARIABLES -------------------------------------------------------------------
    # Dictionnaire des prix (pays | prix en €)
    prices = {
    "Product": "",
    "fr": "",
    "de":"",
    "es":"",
    "it":"",
    "pl":"",
    "nl":"",
    "link_fr":"",
    "link_de":"",
    "link_es":"",
    "link_it":"",
    "link_pl":"",
    "link_nl":"",
    }

    

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
            prices["Product"] = title      
            #print("Product Title : " + title)
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
      if i not in "Product": 
        if not i.startswith("link"):
            splitted_url = URL.split("/")
            
            for idx, val in enumerate(splitted_url):
                if val.startswith("www.amazon"):
                    splitted_url[idx] = "www.amazon." + i
                    caractere="/"
                    final_url= caractere.join(splitted_url)
                    a = "link_"+ i
                    prices[a] = final_url
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
                    price = round(price, 2)
                    prices[i] = price # ajouer le prix courant dans le dictionnaire



    #prices = sort_prices(prices) # Trier les prix par ordre croissant

    #json_prices = json.dumps(prices, indent = 4, ensure_ascii=False) # Dictionnaire prices en format json
    #print(json_prices)

    return jsonify(prices)




if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8000",debug=True)
