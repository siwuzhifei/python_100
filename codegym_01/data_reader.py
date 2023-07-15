import pandas as pd
import datetime as dt
from pandas_datareader import data as pdr
import yfinance as yf
import sqlite3 as sq

yf.pdr_override()

conn = sq.connect('yahoofinance_database')
cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS SA''')
print("Opened database successfully")

start = dt.datetime(2023, 5, 1)
end = dt.datetime(2023, 6, 16)
df = pdr.get_data_yahoo('GOOG', start, end)
# print(df)

df['week'] = df.index.isocalendar().week
print(df)

week_volume_sum = df.groupby('week').Volume.sum()
print(week_volume_sum)

ten = df.resample('10D').mean()
print(ten)

# df.to_sql('google_data', conn, if_exists='replace', index=True)