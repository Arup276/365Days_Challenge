# This program is for get the price of an item from any website



import requests
from bs4 import BeautifulSoup

#Asus zenfone max pro M2 
request = requests.get("https://www.flipkart.com/asus-zenfone-max-pro-m2-blue-64-gb/p/itmfb22gm6tzurvy?pid=MOBFB22GKVVSXN83&srno=b_1_1&otracker=hp_bannerads_3_deskt-homep-2499f_01-01-2019-slot-5_GBS7EOJSKZI5&lid=LSTMOBFB22GKVVSXN83JTTFPW&fm=organic&iid=9f74d8e7-9742-4956-87c3-90bdc86ab1c3.MOBFB22GKVVSXN83.SEARCH&ppt=Homepage&ppn=Homepage&ssid=56gxxf76nk0000001547462649358")
content = request.content
soup = BeautifulSoup(content, "html.parser")
# Inspect :- <div class="_3iZgFn"><div class="_2i1QSc"><div class="_1uv9Cb"><div class="_1vC4OE _3qQ9m1">?14,999</div><div class="_3auQ3N _1POkHg">?<!-- -->17,999</div><div class="VGWI6T _1iCvwn"><span>16% off</span></div></div></div><div class="_1-ZND6"><img class="_3VW0yj" src="//img1a.flixcart.com/www/linchpin/fk-cp-zion/img/info-basic_ea3ba2.svg" id="price-info-icon"></div></div>
element = soup.find("div", {"class": "_1vC4OE _3qQ9m1"})
string_price = element.text.strip()

# to remove the pricw symbol
string_price = string_price[1:]

# To remove the ',' coma from price
if ',' in string_price:
    price = string_price.replace(',', '')
and finally the price
price = int(price)

if price < 14000:
    print("Buy the phone and the price is :", price)
else:
    print("Don't buy its out of your price range ")
