# Members - Riley Atkinson, Zay Ya Min Yin, Amjad Abdallah

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2014,1,1)
end = dt.datetime(2019,12,31)

df = web.DataReader('MSFT', 'yahoo', start, end)

df.to_csv('microsoft.csv')

df = pd.read_csv('microsoft.csv', parse_dates=True, index_col=0)

#print(df)

print(df[['Open','High']].head())

df['Adj Close'].plot()
plt.show()