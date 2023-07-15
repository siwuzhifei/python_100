import pandas as pd
import datetime
import sqlite3 as sq

data_url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data"

data = pd.read_csv(data_url, sep='\s+', parse_dates=[[0, 1, 2]])

conn = sq.connect('wind_database')
cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS SA''')


def fix(x):
    year = x.year - 100 if x.year > 2060 else x.year
    return datetime.datetime(year, x.month, x.day)

data['Yr_Mo_Dy'] = data['Yr_Mo_Dy'].apply(fix)
# 在 SQL 数据库中对包含日期时间数据的列进行查询时，可以使用索引来提高查询效率
data.index = pd.to_datetime(data['Yr_Mo_Dy'])
# 取得每个地区风速度统计资料
describe_wind = data.describe()
#改变统计资料的轴线，取得每一天风速最小值，最大值，平均值和标准差
day_states = pd.DataFrame(columns=['min', 'max', 'mean', 'std'])
day_states['min'] = data.min(axis=1, numeric_only=True)
day_states['max'] = data.max(axis=1, numeric_only=True)
day_states['mean'] = data.mean(axis=1, numeric_only=True)
day_states['std'] = data.std(axis=1, numeric_only=True)
# print(day_states)

# 每个地区一月的平均风速
Jan_mean = data.loc[data.index.month == 1].mean()

# 每个地区每一年每一月的平均风速 用periodindex来统计
eachmonth = data.index.to_period('M')
everymonth_mean = data.groupby(eachmonth).mean()
everymonth_mean.to_sql('eachmonth_wind', conn, if_exists='replace', index=False)
# 用periodindex来统计 每个地区每一年每一月的平均风速， 最小风速和最大风速
monthly = data.groupby(eachmonth).agg(['mean', 'min', 'max'])
#前12笔资料
head12 = monthly.loc[monthly.index[0:12], 'RPT':'KIL']
print(head12)


# 每个地区每一年每一周的平均风速
eachweek = data.index.to_period('W')
everyweek_mean = data.groupby(eachweek).mean()
weekly = data.groupby(eachweek).agg(['mean', 'min', 'max'])
print(weekly)