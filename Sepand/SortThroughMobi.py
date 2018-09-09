import os
import csv
# import pandas as pd
# import numpy as np


# Here we take the data from the mobi usage and find unique pairs of
# intersection points and count their appearances.
file = open('Misc-Bikeshare-usage-BikeShareData_2018.csv', 'r')
reader = csv.reader(file, delimiter=',')
uniquePairs = {tuple(("", "")) : 1 }

for row in reader:
    if tuple((row[3], row[4])) in uniquePairs:
        uniquePairs[tuple((row[3], row[4]))]
    elif tuple((row[4], row[3])) in uniquePairs:
        uniquePairs[tuple((row[4], row[3]))] += 1
    else:
        uniquePairs[tuple((row[3], row[4]))] = 1

for k, v in uniquePairs.items():
    # print(v)

# This translation is supposed to take the values of the

fileTranslateKey = open('/Users/Sepand/Documents/_Development/_Hackathons/VanquishCollisions/VANquish-Bike-Accidents.bike_traffic_flow.csv', 'r')
readerTranslater = csv.reader(file, delimiter=',')
uniquePairsLatLon = {tuple(("", "")) : 1 }

# for row in readerTranslater:
#     if tuple((row[3], row[4])) in uniquePairsLatLon:
#         uniquePairs[tuple((row[3], row[4]))]
#     elif tuple((row[4], row[3])) in uniquePairsLatLon:
#         uniquePairs[tuple((row[4], row[3]))] += 1
#     else:
#         uniquePairs[tuple((row[3], row[4]))] = 1
#
# for k, v in uniquePairs.items():
#     print(v)

#Modify a line
# lines[2][1] = '30'

writer = csv.writer(open('Output.csv', 'w'))
writer.writerows(lines)

# Make a get request to get the latest position of the international space station from the opennotify api.
# response = requests.get("http://api.open-notify.org/iss-now.json")
key = "2b0f4915-576f-4c40-b521-ff1cd2feca1f"
response = requests.get("https://graphhopper.com/api/1/route?point=" + start + "&point=" + finish + "&locale=en&key=2b0f4915-576f-4c40-b521-ff1cd2feca1f")

# Print the status code of the response.
print(response.status_code)

writer = csv.writer(open('Output.csv', 'w'))
writer.writerows(lines)
