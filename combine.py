import pandas as pd
import numpy as np

def read(filename):
    df = pd.read_csv(filename)
    df['Modes'] = 'null'
    num = list(df.index)
    for each in num:
        a = df.loc[each, 'Pedestrian']
        if a == 1:
            df.loc[each, 'Modes'] = 'Single Ped'
        b = df.loc[each, 'Bike']
        if b == 1:
            df.loc[each, 'Modes'] = 'Single Cyl'
        c = df.loc[each, 'Motorcycle']
        if c == 1:
            df.loc[each, 'Modes'] = 'Single Mot'
        d = df.loc[each, 'Veh']
        if d == 1:
            df.loc[each, 'Modes'] = 'Single Veh'

    df.to_csv(filename.split('.')[0] + 'edited.csv')

def combine():
    df1 = pd.read_csv('/Users/Amelia/Desktop/CDedited.csv')
    df2 = pd.read_csv('/Users/Amelia/Desktop/injury.csv')
    df1.append(df2)
    df1.to_csv('/Users/Amelia/Desktop/final.csv')

def main():
    combine()
    #read('/Users/Amelia/Desktop/CD.csv')


if __name__ == '__main__':
    main()