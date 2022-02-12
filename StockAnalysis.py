import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import STL

df = pd.read_csv('csv/BTC-USD.csv', header=0)
x = df['Date']
y = df['Open']

plt.plot(x, y)
plt.xticks(np.arange(0, len(x), 365), [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])


def adfuller_test(column):
    adf_result = adfuller(column)
    adf_output = pd.Series(adf_result[0:4],
                           index=["Test Statistic", "p-value", "Lags Used", "Number of Observations Used", ], )
    for key, value in adf_result[4].items():
        adf_output["Critical Vlaue (%s)" % key] = value
    return adf_output

def stl_decomposition(column):
    # STL Decomposition aus dem Statsmodels Paket
    res = STL(column, period=365).fit()
    res.plot()
    plt.show()

def make_stationary(column):
    print(adfuller_test(column)[1])
    while adfuller_test(column)[1] > 0.05:
        column = column.diff().dropna()
    return column


y_stationary = make_stationary(y)
plt.plot(y_stationary)
plt.show()

stl_decomposition(y)

