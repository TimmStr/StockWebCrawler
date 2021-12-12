import requests
from bs4 import BeautifulSoup
from datetime import datetime
#für sleep
import time

#

def getData(symbol):
    headers ={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}
    url = f'https://de.finance.yahoo.com/quote/{symbol}'

    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.text,'html.parser')
    stock = {'symbol' : symbol,
            'Datum' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'price' : soup.find('div',{'class':'D(ib) Mend(20px)'}).find_all('span')[0].text,
            'change' : soup.find('div',{'class':'D(ib) Mend(20px)'}).find_all('span')[1].text
            } 

    return stock


liste=['AMZN','AAPL','MSFT','BABA','TCEHY','BTC-USD','0LND.SG']

i=0
while i < 10:
    for obj in liste:
        datei = obj+'.csv'
        inhalt = str(getData(obj))
        with open (datei,'a') as f:
            f.write(inhalt)
        print(getData(obj))
    time.sleep(300)
    i=i+1

