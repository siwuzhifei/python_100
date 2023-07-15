import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
print(len(temp_list))
ave_temp = sum(temp_list) / len(temp_list)


# average in pandas has mean funtion
ave_temperature = data["temp"].mean()
print(ave_temp)
# 'list' object has no attribute 'mean' so can not use temp_list call mean()

# get max value
print(data["temp"].max())

# get Data in columns. first line is default a = b in pandas
a = data["condition"]
b = data.condition

# Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data_create = pandas.DataFrame(data_dict)
data_create.to_csv("new_data.csv")