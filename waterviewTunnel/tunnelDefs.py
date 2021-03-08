import datetime


# noinspection PyUnboundLocalVariable
def mergeDupes(oldList):
    newList = []
    for f, item in enumerate(oldList):
        plate = item[0]
        entry = item[1]
        for o in range(f + 1, len(oldList)):
            if oldList[o][0] in plate:
                depart = oldList[o][1]
                break
            else:
                depart = None
        newList.append([plate, entry, depart])
    for i, item in enumerate(newList):
        for x in range(i + 1, len(newList)):
            if newList[x][0] in item[0]:
                newList.pop(x)
                break
    return newList


def calculateDuration(entryTime, exitTime):
    entryTimes, exitTimes = entryTime.split(":"), exitTime.split(":")
    entry = datetime.time(int(entryTimes[0]), int(entryTimes[1]), int(entryTimes[2]))
    leave = datetime.time(int(exitTimes[0]), int(exitTimes[1]), int(exitTimes[2]))
    entryDelta = datetime.timedelta(hours=entry.hour, minutes=entry.minute, seconds=entry.second)
    exitDelta = datetime.timedelta(hours=leave.hour, minutes=leave.minute, seconds=leave.second)
    duration = exitDelta - entryDelta
    return duration


def calculateSpeed(time, distance):
    total_seconds = time.total_seconds()
    hours = (total_seconds / 3600)
    speed = (distance / 1000) / hours
    return speed
