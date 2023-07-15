import pandas as pd

#导入资料
euro = pd.read_csv('https://raw.githubusercontent.com/Code-Gym/python-dataset/master/Euro_2012_stats_TEAM.csv',
                   sep=',')


# 确认所以列的名称和数据类型
euro.dtypes

#列出每一队的黄牌和红牌的数量
cards = euro[['Team', 'Yellow Cards', 'Red Cards']]

#根据黄牌的数量降幂排序，ascending参数是升幂的意思
cards.sort_values('Yellow Cards', ascending=False)

#取得Goals总得分的平均分数
euro.Goals.mean()
#四舍五入, python自带函数round
round(euro.Goals.mean())

# 寻找得分大于5的球队
print(euro[euro.Goals > 5])

# 寻找名字S开头的球队
euro[euro.Team.str.startswith('S')]

# 切割第1-5行中1到5列的资料 切割器iloc 用行列名称切割
print(euro.iloc[0:5, 0:5])

# 切割第1-5行中1到5列的资料 切割器loc切割索引值
loc_euro = euro.loc['0':'3', 'Team':'Goals']
print(loc_euro)