import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


df = pd.read_csv('csv/BTC-USD.csv', header=0)
x = df['Date']
y = df['Open']

plt.plot(x, y)
plt.xticks(np.arange(0, len(x), 365), [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
plt.show()
