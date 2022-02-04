import requests
from bs4 import BeautifulSoup
from datetime import datetime
# für sleep
import sys
import time
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='achilleus',
    password='achilleus',
    database='Aktien'
)

mycursor = mydb.cursor()



def transformData(stock_value):
    compare_list=['0','1','2','3','4','5','6','7','8','9']
    return_value=''
    for i in range(0,len(stock_value)):
        if(stock_value[i] not in compare_list):
            if(stock_value[i]==','):
                return_value=return_value+'.'
            elif(stock_value[i]=='-'):
                return_value=return_value+'-'
        else:
            return_value=return_value + stock_value[i]
    return return_value
    


def getData(symbol):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}
    url = f'https://de.finance.yahoo.com/quote/{symbol}'

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    name = symbol
    date = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    price = transformData(soup.find('div',{'class': 'D(ib) Mend(20px)'}).find('fin-streamer').text)
    price_change = transformData(str(soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[0].text))
    price_change_percent = transformData(str(soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')[1].text))
    


    sql = "INSERT INTO Aktieninfos (Name, Datum, Preis, Aenderung, AenderungPro) VALUES (%s, %s, %s, %s, %s)"
    val = (name, date, price, price_change, price_change_percent)
    mycursor.execute(sql,val)
    mydb.commit()

 





liste = ['AMZN', 'AAPL', 'MSFT', 'BABA', 'TCEHY', 'BTC-USD', 'ETH-USD']

i = 1
while i <= 99999999:
    for obj in liste:
        getData(obj)
        #sys.exit()
    time.sleep(300)
    i = i + 1
