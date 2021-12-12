liste = ['AMZN','AAPL','MSFT','BABA','TCEHY','BTC-USD','0LND.SG']


for li in liste:
    print()
    print(li)
    obj = li+".csv"
    #file = open("AMZN.csv","r")
    file =open(obj,"r")
    for line in file:
        print(line)
    file.close()
    print()
