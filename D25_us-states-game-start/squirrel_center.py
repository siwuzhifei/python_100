import pandas
import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_number = data[["Primary Fur Color", "Hectare Squirrel Number"]]
# print(color_number)

print(data.groupby("Primary Fur Color")["Hectare Squirrel Number"].sum())

gray_number = color_number[color_number["Primary Fur Color"] == "Gray"]
cinnamon_number = color_number[color_number["Primary Fur Color"] == "Cinnamon"]
black_number = color_number[color_number["Primary Fur Color"] == "Black"]
gray_sum = gray_number.sum()
cinnamon_sum = cinnamon_number.sum()
black_sum = black_number.sum()

# grey_count = len(data[data["Primary Fur Color"] == "Gray"])
# print(grey_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_sum, cinnamon_sum, black_sum]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")