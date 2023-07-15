import pandas as pd

chipo = pd.read_csv('https://raw.githubusercontent.com/Code-Gym/python-dataset/master/chipotle.tsv',
                    sep='\t')

#查看所有列的数据类型
print(chipo.dtypes)

#将item_price内的数值从str 转为float类型
price = [float(value[1:]) for value in chipo.item_price]
chipo.item_price = price
print(chipo.dtypes)
#计算item_price的平均值
print(round(chipo.item_price.mean()))

#计算item_price大于7
print(chipo[chipo.item_price >7])
#找出choice_description含有 'Fresh Tomato Salsa'字串的资料
fts = chipo.choice_description.str.contains('Fresh Tomato Salsa')

fts_price7 = chipo[(chipo.item_price >7 ) & (fts==True)]
print(fts_price7)

#找出item_price最贵的一笔资料
print(chipo.sort_values(by=['item_price'], ascending=False).head(1))

# print(chipo.iloc[3:11, 0:3])
#print(chipo.loc[3:10, 'order_id':'item_name'])