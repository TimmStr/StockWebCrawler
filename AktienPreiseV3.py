import requests
from bs4 import BeautifulSoup
from datetime import datetime
#für sleep
import time
import mysql.connector

mydb = mysql.connector.connect(
        host='localhost',
        user ='achilleus',
        password='achilleus',
        database ='Aktien'
        )

mycursor = mydb.cursor()

def getData(symbol):
    headers ={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}
    url = f'https://de.finance.yahoo.com/quote/{symbol}'

    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.text,'html.parser')
    
   
    name = symbol
    datum = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    preis = str(soup.find('div',{'class':'D(ib) Mend(20px)'}).find_all('span')[0].text)
    aen = str(soup.find('div',{'class':'D(ib) Mend(20px)'}).find_all('span')[1].text)
    aenumw = ""
    aenumw1 = ""
    preisumw = ""

    #Preis umwandeln
    j=0
    while j < len(preis):
        #if preis[j] =="+" or preis[j] =="-":
        #    j=j+1
        #    continue
        if preis[j] == ",":
            preisumw = preisumw + "."
            j=j+1
        elif preis[j] == ".":
            j=j+1
            continue
        else:
            preisumw =preisumw+ preis[j]
            j=j+1
    #print("Preis: "+preisumw)

    i=0
    #erster Teil aen
    while aen[i] != " ":
        #if aen[i] == "+" or aen[i]=="-":
        #    i=i+1
        #    continue
        if aen[i] == ",":
            aenumw = aenumw + "."
            #print(aenumw)
            i=i+1
        elif aen[i] == ".":
            i=i+1
            continue
        elif aen[i] == "%":
            break
        else:
            aenumw = aenumw + aen[i]
            i=i+1
    #print("Change 2: "+aenumw)
    #zweiter Teil aen 
    c=i+1
    counter = -1
    while c < len(aen) or counter != 0:
        counter =counter -1
        if aen[c] == "(":
            c=c+1
            continue
        if aen[c] == ",":
            aenumw1 = aenumw1 + "."
            #print(aenumw1)
            counter = 2
            c=c+1
        elif aen[c] == "%":
            break
        else:
            aenumw1 = aenumw1 + aen[c]
            c=c+1
    






    #print(name+ " "+" "+preis+" "+ aenumw)
    sql = "INSERT INTO Aktieninfos (Name, Datum,Preis, Aenderung, AenderungPro) VALUES ('"+name+"','"+datum+"','"+preisumw+"','"+aenumw+"','"+aenumw1+"')"
    mycursor.execute(sql)
    mydb.commit()
    
liste=['AMZN','AAPL','MSFT','BABA','TCEHY','BTC-USD','ETH-USD']

i=1
while i <= 999999 :
    for obj in liste:
        getData(obj)
    time.sleep(300)
    i=i+1
