import datetime
from custom.cars import *
from custom.globals import *


def checkNum(x):
    # simple error checking for a number lower than 2400
    try:
        int(x)
        if int(x) > 2400:
            return True
        else:
            raise ValueError("Too small of a number")
    except ValueError:
        return False


def mergeDupes(oldList):
    # returns a finished list with a list containing
    # [carPlate, entryTime, exitTime]  for easy calculations.
    newList = []
    for f, item in enumerate(oldList):
        plate = item[0]
        try:
            entry = item[1]
            for o in range(f + 1, len(oldList)):
                if oldList[o][0] in plate:
                    depart = oldList[o][1]
                    break
                else:
                    depart = '00:00:00'
            newList.append([plate, entry, depart])
        except IndexError:
            errors.append("{} doesn't have times".format(item[0]))
    for i, item in enumerate(newList):
        for x in range(i + 1, len(newList)):
            if newList[x][0] in item[0]:
                newList.pop(x)
                break
    return newList


def changeLength():
    # Function that lets the user change the distance between the two
    # gantries with error checking for if it is a whole number below 2400
    isNum = False
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
                print("that isn't a valid input,"
                      " check if it is a number more than 2400")
                continue


def createCars(data, distance):
    # This function uses my custom Car class:
    # and then creates and appends instances of this class to a list.
    instances = []
    for i, column in enumerate(data):
        duration = calculateDuration(column[1], column[2])
        instances.append(Car(column[0], column[1], column[2], duration,
                             calculateSpeed(duration, distance),
                             calculateFines(calculateSpeed(duration,
                                                           distance))))
    return instances


def calculateDuration(entryTime, exitTime):
    # Function that returns duration using time and timedelta modules
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
    # Function that turns duration and distance to km/h
    total_seconds = time.total_seconds()
    hours = (total_seconds / 3600)
    speed = (distance / 1000) / hours
    return speed


def calculateFines(speed):
    # Function that calculates fines and appends correct fine to car,
    speedOver = speed - speedLimit
    if speedOver <= 0:
        return None
    elif speedOver > fineRanges[len(fineRanges) - 1][0]:
        return fines[len(fines) - 1]  # return the last fine in the list
    else:
        for i, x in reversed(list(enumerate(fineRanges))):
            if speedOver >= fineRanges[i][0]:
                return fines[i]


def checkForErrors(speeders, errorList):
    # This function checks for potential errors and flags cars
    # -  if the car takes longer than 4 mins to exit the tunnel
    # -  if the car was going at over 200km/h as that seems unreasonable
    # -  if the car was going below 0km/h( meaning that it didn't exit)
    muckUps = errorList
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
    # This is the output function that will print out the outputs nicely
    # and will also append the fined cars and errors to the desired Errorfile
    errorFile = open('custom/' + errorPath + '.txt', 'w+')
    print("licence", "entryTime", "exitTime", " duration",
          "  speed", "\tfines")
    for car in instances:
        if car.fine is not None:
            errorFile.write("{} \twas fined {}\n"
                            .format(car.license, car.fine))
        print("{} \t{}  {}  {}  "
              "{:.2f}km/h\t {}".format(car.license, car.entryTime,
                                       car.exitTime, car.duration,
                                       car.speed, car.fine))
    for error in mistakes:
        errorFile.write(error + '\n')
        print(error)
    errorFile.close()
