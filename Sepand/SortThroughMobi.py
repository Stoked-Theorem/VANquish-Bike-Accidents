import os
import csv
# import pandas as pd
# import numpy as np
#
# df = pd.reader(/Users/Sepand/Documents/_Development/_Hackathons/VanquishCollisions/VANquish-Bike-Accidents/Sepand/Misc-Bikeshare-usage-BikeShareData_2018.csv))
# print(df)
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
    print(v)
# writer = csv.writer(file, delimiter=',')
