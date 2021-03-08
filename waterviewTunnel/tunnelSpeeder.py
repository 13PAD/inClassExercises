import csv
from cars import *
from tunnelDefs import *

filePath = "tunnelTimes.csv"
fileData, rows, totalRows = '', '', ''
cars = []
distance = 2690

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

for i, column in enumerate(rows):
    duration = calculateDuration(column[1], column[2])
    cars.append(Car(column[0], column[1], column[2], duration, calculateSpeed(duration, distance), ''))

print("{} {} {} {} {}\t{}".format("licence", "entryTime", "exitTime", "duration", "speed", "fines"))
for car in cars:
    print("{} \t{}  {}  {}  {:.2f}km/h\t{}".format(car.license, car.entryTime, car.exitTime, car.duration, car.speed, 0))
