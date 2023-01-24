# with open("weather_data.csv", mode="r") as file:
#     data = []
#     myData = file.readlines()

#     data.append()
# print(data)
import cvs
with open("weather_data.csv", mode="r") as file:
    data = cvs.reader(file)
