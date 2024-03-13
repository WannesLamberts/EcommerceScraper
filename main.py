import requests
from bs4 import BeautifulSoup
from product import *
from Utils import *
import json
#ALLE CLASSES VOOR BELANGRIJKE INFO
#TAG a CLASS q84f1m CKDt_l LyRfpJ JT3_zV CKDt_l _2dqvZS -> vakje in winkel
#TAG span CLASS sDq_FX lystZ1 FxZV-M HlZ_Tf -> prijs product (moet nog extra geparsed worden op prijs
#TAG h3 CLASS FtrEr_ lystZ1 FxZV-M HlZ_Tf ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2 -> merk
#TAG h3 CLASS sDq_FX lystZ1 FxZV-M HlZ_Tf ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2 -> productNAAM
#TAG img CLASS sDq_FX lystZ1 FxZV-M _2Pvyxl JT3_zV EKabf7 mo6ZnF _1RurXL mo6ZnF _7ZONEy -> foto
products = []
images = []
for x in range(1,5):
    website = "https://www.zalando.be/kleding/?p="+str(x)
    r = requests.get(website)
    soup = BeautifulSoup(r.content, 'html.parser')
    objecten = soup.find_all("a",class_="q84f1m CKDt_l LyRfpJ JT3_zV CKDt_l _2dqvZS")
    for object in objecten:
        prijs = object.find("span",class_="sDq_FX lystZ1 FxZV-M HlZ_Tf")
        if prijs==None:
            prijs=-1
        else:
            prijs = prijs.text.strip()
        merk = object.find("h3",class_="FtrEr_ lystZ1 FxZV-M HlZ_Tf ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2").text.strip()
        productNaam = object.find("h3",class_="sDq_FX lystZ1 FxZV-M HlZ_Tf ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2").text.strip()
        prod=Product(productNaam,merk,prijs)
        products.append(prod)
    #KVKCn3 u-C3dd jDGwVr mo6ZnF KLaowZ
    imagesObject = soup.find_all("img",class_="sDq_FX lystZ1 FxZV-M _2Pvyxl JT3_zV EKabf7 mo6ZnF _1RurXL mo6ZnF _7ZONEy")
    for img in imagesObject:
        if "/article/" in img['src']:
            images.append(img['src'])
ToJson(products,images)
f = open("products.json")
data = json.load(f)
print(data)