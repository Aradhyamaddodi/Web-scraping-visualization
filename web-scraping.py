import requests
from bs4 import BeautifulSoup
import pandas as pd

Product_names = []
Prices        = []
Descriptions  = []
Reviews       = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

for i in range(2,12):

    url   = "https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobiles%7CMobiles&requestId=18e8ee3c-82fc-4fdf-b22d-9d93b4a01bb1&page"+str(i)

    r     = requests.get(url, headers=headers)

    soup  = BeautifulSoup(r.text, 'html.parser')
    box   = soup.find("div", class_ = "_1YokD2 _3Mn1Gg")

    names = box.find_all("div", class_ = "_4rR01T")
    # print(len(names))
    for i in names:
        name = i.text
        Product_names.append(name)
    # print(len(Product_names))
        
    prices = box.find_all("div",class_ = "_30jeq3 _1_WHN1")
    for i in prices:
        name = i.text
        Prices.append(name)
    # print(len(prices))

    desc = box.find_all("ul", class_ = "_1xgFaf") 

    for i in desc :
        name = i.text
        Descriptions.append(name)
    # print(len(Descriptions))

    reviews = box.find_all("div", class_ = "_3LWZlK") 
    for i in reviews:
        name = i.text
        Reviews.append(name)
    # print(len(Reviews))

df = pd.DataFrame({"Product Name":Product_names, "Price":Prices,"Description":Descriptions,"Reviews":Reviews })
# print(df)

df.to_csv("C:/Users/aradh/OneDrive/Desktop/flipkart/mobiles.csv")
