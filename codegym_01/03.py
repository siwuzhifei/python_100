import pandas as pd
import sqlite3 as sq

conn = sq.connect('test_database')
cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS SA''')
print("Opened database successfully")


users = pd.read_csv('https://raw.githubusercontent.com/Code-Gym/python-dataset/master/u.user.txt',
                    sep='|',
                    index_col='user_id')
# 把CSV文件导出到本地
# users.to_csv("d:/XIAOYAN//users.csv",sep=",", index=True, header=True)
# 把文件导出到sqlite
users.to_sql('users_data', conn, if_exists='replace', index=False)


#每个职业的平均年龄
occupation_mean = users.groupby('occupation').age.mean()

#每个职业的年龄最小值，最大值，平均值和人数
age_count = users.groupby('occupation').age.agg(['min', 'max', 'mean', 'count'])
print(age_count)

age_mean = users.groupby('occupation').agg({'age':'mean'})
age_mean.to_sql('age_mean', conn, if_exists='replace', index=False)
# age_mean.to_csv("d:/XIAOYAN//age_mean.csv",sep=",", index=True, header=True)
# print(age_mean)
#取得每个职业和性别的年龄平均和数量
age_gender = users.groupby(['occupation', 'gender']).agg({'age':'mean', 'gender':'count'})
age_gender.to_sql('age_gender', conn, if_exists='replace', index=False)


#建立函数，把性别转为数字，用apply执行函数,把执行结果存入新的一个columna中

def gender_to_numeric(x):
    if x == 'M':
        return 1
    elif x == 'F':
        return 0

users['gender_n']= users['gender'].apply(gender_to_numeric)

#计算每个职业中男性所占比例，并且降序排列
result = users.groupby('occupation').gender_n.sum()/users.occupation.value_counts() * 100
print(result.sort_values(ascending=False))