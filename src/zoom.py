import pandas as pd
import datetime as date
import time

identityData = pd.read_csv("canvasintel.csv")
zoomData = pd.read_csv("participants_88187808697.csv")
merged_data = identityData.merge(zoomData, on=["Name (Original Name)"]).set_index('asuid')


def exists(studentID):
    counter = 0
    y = merged_data.index.tolist()
    for id in y:
        if studentID == id:
            counter += 1

    if counter == 1:
        return True

    else:
        return False
    

def getId():
    y = identityData['asuid'].tolist()
    return y


def startTime(studentID):
    if exists(studentID):
        y = str(merged_data.at[studentID, 'Join Time'])
        x = str(date.datetime.now().date()) + "T" + y[11:16] + ":00"
        z = date.datetime.fromisoformat(x)
        unixStartTime = int(time.mktime(z.timetuple()))
        return unixStartTime
    else:
        return 0


def endTime(studentID):
    if exists(studentID):
        y = str(merged_data.at[studentID, 'Leave Time'])
        x = str(date.datetime.now().date()) + "T" + y[11:16] + ":00"
        z = date.datetime.fromisoformat(x)
        unixEndTime = int(time.mktime(z.timetuple()))
        return unixEndTime
    else:
        return 0
