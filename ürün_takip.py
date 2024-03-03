import requests
from bs4 import BeautifulSoup
import time

def urun_kontrol():
    url = "https://www.amazon.com.tr/HP-Diz%C3%BCst%C3%BC-Bilgisayar-i5-13500H-7N9V3EA/dp/B0BYJWZKYH/ref=sr_1_2?__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3Q3H39IBUDTYH&dib=eyJ2IjoiMSJ9.vz99PFy0e3ZHYelKBW0Xc764AG4118Wk6siZXsSSeguM4YwZP4_VZ-3qQeUJJAFMgnk9xozNN5X4vcS_VHvQQ-mJkBs6VYONyrpW3mL5kJoFl0VJt4Y_beIl1x6bWexMBCaVoFkW0au0e6ZU6KcBKZPByCh7Q6nmx_xn40htlAtoy9vesoMpdpyJMShS5WHA9s6dFW1umo-j3l0gfaYl6mdUdD5xRTl002L0Zh0IUJtPchu7d5PbOnXVPrc90MmV2fcW6lWRTcO02F9aqEnPCQtfeX2bnItuxU6aO2Jrz_8.bb2ErMeDnisP5NT7h4K-JGrmy--RQz241sNKnKyEt1E&dib_tag=se&keywords=bilgisayar&qid=1709489780&sprefix=bilgisayar%2Caps%2C209&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")

    bilgiler = soup.find(id="productTitle").text.strip()

    fiyat = soup.find("span", class_="a-price-whole").text.strip()
    fiyat = int(fiyat.replace(".", "").replace(",", ""))  
    if (fiyat < 31000):
        print(f"{fiyat} TL olan {bilgiler} fiyatı düştü!!!")

    else:
        print(f"{fiyat} TL olan {bilgiler} halen aynı maalesef ama umut kesilmez")


while(True):
    urun_kontrol()
    time.sleep(5)





