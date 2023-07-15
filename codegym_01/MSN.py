import pandas as pd
import sqlite3 as sq

data_url = 'https://raw.githubusercontent.com/Code-Gym/python-dataset/master/msg.txt'

data = pd.read_csv(data_url,
                   sep='\t',
                   names=['status', 'msg'])

# 把status栏转为大写, 用pandas.Series功能， python自带功能upper是处理单独一行
data['status'].str.upper()
# 把 msg 栏转为首字母大写, 用pandas.Series功能，
data['msg'].str.title()

# 把 status栏内容替换replace('原始内容’， ‘替换内容’）
# data['status'].str.replace('ham', 'not spam')

#python内置功能split()
data['msg'].str.split(',')

#筛选

data.loc[data['msg'].str.startswith('a')]
# 或者 data[data['msg'].str.startswith('a')]

#过滤不是垃圾信的讯息,包含英文单词'OK‘
ham = data[data['status']== 'ham']
mask = ham['msg'].str.contains('OK')

print(ham[mask])

#过滤不是垃圾信的讯息,'L'开头
mask1 = ham['msg'].str.startswith('L')
#print(ham[mask1])