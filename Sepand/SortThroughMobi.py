import os
import csv
import requests
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

# for k, v in uniquePairs.items():
#     print()

# This translation is supposed to take the values of the intersections and
# and place their equivalent lat lon 2 cells over, using the bike_traffic_flow file
# that contains a table to translate with.
fileTranslateKey = open('../bike_traffic_flow.csv', 'r')
readerTranslater = csv.reader(file, delimiter=',')
# uniquePairsLatLon = {tuple((0, 0)) : 1 }

lines = list(reader)

for row in reader:
    #Translate the first intersection at row[0]
    for rowTranslate in readerTranslater:
        if rowTranslate[0] == row[0]: #if the names match
            lines[row][3] = rowTranslate[2]
            lines[row][4] = rowTranslate[3]
    #Translate the second intersection at row[1]
    for rowTranslate in readerTranslater:
        if rowTranslate[0] == row[0]: #if the names match
            lines[row][5] = rowTranslate[2]
            lines[row][6] = rowTranslate[3]

# for k, v in uniquePairsLatLon.items():
    # print(k, v)

#Modify a line
# lines[2][1] = '30'

writer = csv.writer(open('Misc-Bikeshare-usage-BikeShareData_2018.csv', 'w'))
writer.writerows(lines)

# Make a get request to get the latest position of the international space station from the opennotify api.
# response = requests.get("http://api.open-notify.org/iss-now.json")
# key = "2b0f4915-576f-4c40-b521-ff1cd2feca1f"
# response = requests.get("https://graphhopper.com/api/1/route?point=" + start + "&point=" + finish + "&locale=en&key=2b0f4915-576f-4c40-b521-ff1cd2feca1f")
#
# # Print the status code of the response.
# print(response.status_code)
#
# writer = csv.writer(open('Output.csv', 'w'))
# writer.writerows(lines)
