import datetime
from custom.cars import *
from custom.globals import *


def checkNum(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


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
                depart = '00:00:00'
        newList.append([plate, entry, depart])
    for i, item in enumerate(newList):
        for x in range(i + 1, len(newList)):
            if newList[x][0] in item[0]:
                newList.pop(x)
                break
    return newList


def changeLength():
    isNum = False
    distance = 2690
    while not isNum:
        inputtedDistance = input("enter a new distance or"
                                 " press enter to use default")
        if inputtedDistance == '':
            return 2690
        else:
            isNum = checkNum(inputtedDistance)
            if isNum:
                return int(inputtedDistance)
            else:
                continue


def createCars(data, distance):
    instances = []
    for i, column in enumerate(data):
        duration = calculateDuration(column[1], column[2])
        instances.append(Car(column[0], column[1], column[2], duration,
                             calculateSpeed(duration, distance),
                             calculateFines(calculateSpeed(duration,
                                                           distance))))
    return instances


def calculateDuration(entryTime, exitTime):
    entryTimes, exitTimes = entryTime.split(":"), exitTime.split(":")
    entry = datetime.time(int(entryTimes[0]), int(entryTimes[1]),
                          int(entryTimes[2]))
    leave = datetime.time(int(exitTimes[0]), int(exitTimes[1]),
                          int(exitTimes[2]))
    entryDelta = datetime.timedelta(hours=entry.hour, minutes=entry.minute,
                                    seconds=entry.second)
    exitDelta = datetime.timedelta(hours=leave.hour, minutes=leave.minute,
                                   seconds=leave.second)
    duration = exitDelta - entryDelta
    return duration


def calculateSpeed(time, distance):
    total_seconds = time.total_seconds()
    hours = (total_seconds / 3600)
    speed = (distance / 1000) / hours
    return speed


def calculateFines(speed):
    speedOver = speed - speedLimit
    if speedOver <= 0:
        return None
    elif speedOver > fineRanges[len(fineRanges) - 1][0]:
        return fines[len(fines) - 1]  # return the last fine in the list
    else:
        for i, x in reversed(list(enumerate(fineRanges))):
            if speedOver >= fineRanges[i][0]:
                return fines[i]


def checkForErrors(speeders):
    muckUps = []
    for car in speeders:
        totalSeconds = car.duration.total_seconds()
        speedyBoi = car.speed
        if totalSeconds > 240:
            muckUps.append("{} took too long".format(car.license))
        if speedyBoi > 200:
            muckUps.append("{} was going over 200km/h".format(car.license))
        if speedyBoi < 0:
            muckUps.append("{} didn't exit".format(car.license))
    return muckUps


def outputData(instances, mistakes, errorPath):
    errorFile = open('custom/' + errorPath + '.txt', 'w+')
    print("licence", "entryTime", "exitTime", " duration", "  speed", "\tfines")
    for car in instances:
        if car.fine is not None:
            errorFile.write("{} \twas fined {}\n".format(car.license, car.fine))
        print("{} \t{}  {}  {}  "
              "{:.2f}km/h\t {}".format(car.license, car.entryTime,
                                       car.exitTime, car.duration,
                                       car.speed, car.fine))
    for error in mistakes:
        errorFile.write(error + '\n')
        print(error)
    errorFile.close()
