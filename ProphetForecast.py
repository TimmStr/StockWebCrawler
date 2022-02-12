import pandas as pd
from datetime import datetime
import warnings

# there are often errors when installing prophet in pycharm
# if its not working set up anaconda-env (only tested in jupyter)
from prophet import Prophet

warnings.filterwarnings("ignore")


# calculate prophet for all regions - hard coded years 2006 - 2019, predict 2020
def prophet_all(data):
    df_pr = data[['Date', 'Open']]
    # filter years - from 2006 - 2019
    df_pr = df_pr.iloc[:5114]
    # format columns for prophet
    df_pr.columns = ['ds', 'y']
    # init prophet-model and train with dataframe
    m = Prophet()
    m.fit(df_pr)
    # build future-dataframe
    future = m.make_future_dataframe(periods=365)
    # make forecast based on future-dataframe
    forecast = m.predict(future)
    # plot forecast of 2020
    fig1 = m.plot(forecast,xlabel='Year',ylabel='SQKM')
    fig1.show()
    # plot seasonal components of dataset
    fig2 = m.plot_components(forecast)
    fig2.show()
    # print forecast as table data
    print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

# change header to 1 when you are using jupyter
df = pd.read_csv('csv/BTC-USD.csv', header=0, delimiter=',')


# call prophet for all regions
prophet_all(df)