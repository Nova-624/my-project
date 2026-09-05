
# # with open(r"weather_data.csv") as weather_data:
# #     data = weather_data.readlines()
# #     print(data)

# # import csv

# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     tempretaure = []
# #     for row in data:
# #         if row[1] != "temp":
# #             tempretaure.append(int(row[1]))
# #     print(tempretaure)

# DATA ANALYSIS WITH PANDAS-----------------------------------------------
# import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])

# # Conversion to dict
# # data_dict = data.to_dict()
# # print(data_dict)

# # Conversion of series to a list
# # data_list = data["temp"].to_list()
# # print(data_list)

# # calcualte the average of temperature
# # --there's a mean() to do so

# # avg_temp = data["temp"].mean()
# # print(f"Average Temperature: {avg_temp}")


# # temp = data["temp"].to_list()
# # avg = sum(temp)/ len(temp)
# # print(avg)

# # print(data["temp"].max())

# # Get data in columns
# # print(data["condition"])
# # # OR
# # print(data.condition)

# # Get data in row
# # print(data[data.day == "Monday"])

# # Print the row of data which had the highest temperature
# # max_temp_week = data[data.temp == data["temp"].max()]
# # print(max_temp_week.day) # to tap into a particular column

# # TODO- Convert the Monday's temperature to Farenheit. Hint: use[] to get a single value from the pandas series by index.
# # to convert Celsius to Fahrenheit-- f = (c x 9/5) + 32

# in_celsius = data.temp[0] # monday's temp
# in_fahrenheit = (in_celsius* 9/5) + 32
# # print (f"Monday's temperature in Fahrenheit: {in_fahrenheit} F")

# # How to create a Dataframe from scratch
# data_dict = {"students": ["Angela", "Mary", "Julie"],
#              "scores": [45, 56, 37],
#              }
# data = pandas.DataFrame(data_dict)
# # can convert it to a csv file
# # data.to_csv("new_data.csv")

# TODO - get districts--Gwalior, Indor, Bhopal
# TODO - get the count of cattle in each city
# TODO- Create mp_20th_livestock.csv

import pandas

livestock_data = pandas.read_csv("Livestock_census_20.csv")

# filter mp first
mp_livestock = livestock_data[livestock_data["state_name"] == "Madhya Pradesh"]

# get cities

cities = ["GWALIOR","MORENA","INDORE"]
data_dict = {}

for city in cities:
    result = mp_livestock[mp_livestock["district_name"] == city]["cattle"]
    data_dict[city] = result.item()

# Convert properly
df = pandas.DataFrame(list(data_dict.items()), columns=["district_name", "cattle"])

df.to_csv("cattel_count.csv")
print(df)








