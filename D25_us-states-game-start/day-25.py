# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#              temperatures.append(int(row[1]))
#     print(temperatures)




def Average(a):
    avg = sum(a) / len(a)
    return avg

data = pandas.read_csv("../D24-Mail+Merge+Project+Start/weather_data.csv")
# print(data)
# print(type(data))
# print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
average = Average(temp_list)
print(f"Average of temperatures is {average}")

# or use mean function
print(data["temp"].mean())
print(data["temp"].max())
# 'list' object has no attribute 'mean' so can not use temp_list call mean()


monday = data[data.day == "Monday"]
temp_f = int(monday.temp * 9 / 5) + 32
print(temp_f)
