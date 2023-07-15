import pandas as pd
import sqlite3 as sq

drinks = pd.read_csv('https://raw.githubusercontent.com/Code-Gym/python-dataset/master/drinks.csv',
                    sep=',',
                    index_col='country')

conn = sq.connect('drinks_database')
cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS SA''')
print("Opened database successfully")

drinks.to_sql('drinks_data', conn, if_exists='replace')

beer_mean = drinks.beer_servings.mean()
print(beer_mean)
group_beer_mean = drinks.groupby('continent').beer_servings.mean()
print(group_beer_mean)
group_wine = drinks.groupby('continent').wine_servings.agg(['max', 'min','mean', 'count'])
print(group_wine)