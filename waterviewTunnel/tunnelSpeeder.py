import csv
from tunnelDefs import *
from globals import *
try:
    with open(filePath) as csvfile:
        fileData = csv.reader(csvfile, delimiter=',')
        next(fileData)
        rows = sorted(fileData)
        totalRows = len(rows)
except FileNotFoundError:
    print("{} not found".format(filePath))
    quit()
rows = mergeDupes(rows)
cars = createCars(rows)
print("licence", "entryTime", "exitTime", "duration", "speed", "fines")
for car in cars:
    print("{} \t{}  {}  {}  {:.2f}km/h\t{}".format(car.license, car.entryTime,
                                                    car.exitTime, car.duration, car.speed, car.fine))
