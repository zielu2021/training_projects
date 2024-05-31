import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures= []
#     for row in data:
#         # temperature = row[1]
#         # temperatures.append(temperature)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

# import pandas
# data =pandas.read_csv("weather_data.csv")
# print(data)
# # print(data["temp"])
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# # average_temp =
#
#
# average_temp = sum(temp_list) / len(temp_list)
# final_number = round(average_temp,2)
# print(final_number)
#
# average_t = data["temp"].mean()
# print(average_t)
#
# max_t = data["temp"].max()
# print(max_t)

# print(data[data.temp ==data.temp.max()])
# print(data)

# get data in column
# print(data["temp"])
# print(data.temp)

# get data in row
# print(data[data["day"] == "Tuesday"])
# print(data[data.day == "Monday"])


# print(data[data.temp == data.temp.max()])
#
# print(data[data.temp == data.temp.min()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# create data frame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela", "szczepan"],
#     "scores": [76, 56, 65, "-"]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import csv
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrel_count)
# print(red_squirrel_count)
# print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]

}

print(data_dict)

df= pandas.DataFrame(data_dict)
# print(data)
df.to_csv("squirrel_data")