import pandas as pd
from sqlalchemy import create_engine
import pymysql

#SQL Connection Informations
sqlEngine = create_engine('mysql+pymysql://achilleus:achilleus@127.0.0.1:3306')
#SQL Connection
dbConnection = sqlEngine.connect()
#Dataframe befüllen
frame = pd.read_sql('SELECT * FROM Aktien.Aktieninfos',dbConnection);
#frame=pd.read_sql('SELECT Datum ,Preis FROM Aktien.Aktieninfos WHERE Name = "AMZN"',dbConnection);
#DB Connection schließen
dbConnection.close()


#eigentliche Analyse
print(frame)
dat=frame['Datum']
preis=frame['Preis']
frame.to_csv('Aktien.csv')

