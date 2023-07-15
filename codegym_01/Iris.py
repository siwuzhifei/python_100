import pandas as pd
import numpy as np


iris = pd.read_csv('https://raw.githubusercontent.com/Code-Gym/python-dataset/master/iris.csv',
                   names=['sepal_length', 'sepal_width', 'pental_length', 'petal_width','class'])

print(iris.head())

# 删除列 class
# del iris['class']

# 确认DataFrame中是否有空值
iris.isnull().sum()

# 建立空值 在第一行到第三行，sepal_width column之间建立空值
iris.iloc[1:4, 1:2] = np.nan
print(iris.head())
# print(iris.isnull().sum())

# 将DataFrame空值，替换为数字0 fillna()
iris.fillna(0, inplace=True)

# 删除DataFrame中资料为空值的列数 dropna()
# 建立空值 在第一行到第三行，sepal_width column之间建立空值
iris.iloc[1:4, 1:2] = np.nan
iris = iris.dropna(axis='index', how='any')
print(iris.head())

#重新设置索引值 reset_index()

iris = iris.reset_index(drop= True)
print(iris.head())