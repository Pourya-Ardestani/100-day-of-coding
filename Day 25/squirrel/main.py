# import csv
# with open("weather-data.csv") as weather_file:
#     # weather = weather_file.readlines()
#     # for line in weather:
#     #     line.strip()
#     # print(weather)
#     # weather = weather_file.read().split()
#     data = csv.reader(weather_file)
#     temperature = []
#     count = 0
#     for row in data:
#         count += 1
#         if count == 1:
#             continue
#         actual_temperature = int(row[1])
#         temperature.append(actual_temperature)
#     # temperature.pop(0)
#     print(temperature)
#
#

import pandas
data = pandas.read_csv("weather-data.csv")
# temp_list = data["temp"].tolist()
# sum = 0
# for temp in temp_list:
#     sum += int(temp)
# print(sum/len(temp_list))
#
# max_temp = data["temp"].max()
# print(max_temp)

# max_temp = data["temp"].max()
# print(data[data["temp"] == max_temp])
#
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
# print((monday_temp*1.8)+32)

# data = {
#     "Esm": ["ali", "mohammad", "abbas"],
#     "famil": ["gorily", "salamatian", "gorbeee"],
#     "job": ["worker", "-", "employee"],
# }
# data_Frame = pandas.DataFrame(data)
# data_Frame.to_csv("workers_file.csv")

squirrel_data = pandas.read_csv("Squirrel-Data.csv")

#TODO find primary Fur Color for each color
gray_count = 0
red_count = 0
black_count = 0
all_colors = squirrel_data["Primary Fur Color"]
for color in all_colors:
    if color == "Gray":
        gray_count += 1

    elif color == "Cinnamon":
        red_count += 1

    elif color == "Black":
        black_count += 1

#TODO final csv that contains squirrel counts
data = {
     "Fur Color": ["gray", "red", "black"],
     "Count": [gray_count, red_count, black_count],
}
new_data_frame = pandas.DataFrame(data)
new_data_frame.to_csv("squirrel_count.csv")
