import pandas as pd

res = pd.read_csv('https://raw.githubusercontent.com/Code-Gym/python-dataset/master/RestaurantVisitors.csv')

res.index = pd.to_datetime(res['date'])
res['week'] = res.index.isocalendar().week
week_rest1_sum = res.groupby('week').rest1.sum()

holiday_data = res[res.holiday==1]
non_holiday_data = res[res.holiday==0]
print(res.head())
# print(holiday_data.loc[:, 'rest1':'rest4'].mean())
# print(non_holiday_data.loc[:, 'rest1':'rest4'].mean())