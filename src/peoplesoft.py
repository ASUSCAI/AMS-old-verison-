import pandas as pd

df = pd.read_csv("peoplesoft.csv", index_col=['canvas'])

def getCanvasNums():
    y = df.index.tolist()
    return y


def getRoom(x):
    y = df.at[x, 'location']
    return y

def getTimes(x):
    start = df.at[x, 'start']
    end = df.at[x, 'end']
    times = [start, end]
    return times


def getDays(x):
    y = df.at[x, 'days']
    z = str(y)
    lnn = z.split()
    for i in range(len(lnn)):
        if lnn[i] == 'M':
            lnn[i] = 0

        if lnn[i] == 'Tu':
            lnn[i] = 1

        if lnn[i] == 'W':
            lnn[i] = 2

        if lnn[i] == 'Th':
            lnn[i] = 3

        if lnn[i] == 'F':
            lnn[i] = 4

        if lnn[i] == 'Sa':
            lnn[i] = 5

        if lnn[i] == 'Sun':
            lnn[i] = 6
    return lnn
