# Members - Riley Atkinson, Zay Ya Min Yin, Amjad Abdallah

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

#start = dt.datetime(2019,1,1)
#end = dt.datetime(2019,12,31)

#df = web.DataReader('APPL', 'yahoo', start, end)

#df.to_csv('apple.csv')

df = pd.read_csv('microsoft.csv', parse_dates=True, index_col=0)

df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
df.dropna(inplace=True)   

print(df.head())

ax1 = plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
ax2 = plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1, sharex=ax1)

ax1.plot(df.index,df['Adj Close'], 'r', label='Adjusted Close')
ax1.plot(df.index,df['100ma'], 'g', label= "100 Moving Average")
ax1.set_title('Adjusted Close and 100 day Moving Average for Microsoft')
ax1.legend()

ax2.bar(df.index,df['Volume'], label = "Volume", color='b')
ax2.legend()

plt.show()
