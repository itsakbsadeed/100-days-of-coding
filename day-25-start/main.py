# with open("weather_data.csv") as data_file:
#    data = data_file.readlines()
#    print(data)




#  import csv
#
#  with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)

import pandas

#data = pandas.read_csv("weather_data.csv")
#print(data)

#temp_list = data["temp"].to_list
#print(temp_list)
#print(data["temp"].max())

# Get Data in Columns
#print(data["condition"])
#print(data.condition)
# Those two are the same.

 # Get data in Row
#print(data[data.day == "Monday"])

#print(data[data.temp == data.temp.max()])

# Creating data frame from scratch
#data_dict = {
#    "Student": ["Amy", "James", "Angela"],
#    "Score": [76, 56, 65]
#}
 #data = pandas.DataFrame(data_dict)
 #print(data)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")