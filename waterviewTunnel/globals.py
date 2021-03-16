import csv
filePath = "tunnelTimes.csv"
cars = []
length, speed_limit = 2690, 80
fine_ranges = [[0, 10], [11, 15], [16, 20], [21, 25], [26, 30], [31, 35], [36, 40], [41, 45]]
fines = [30, 80, 120, 170, 230, 300, 400, 510, 630]


def getFileData(file):
    try:
        with open(file) as csvfile:
            fileData = csv.reader(csvfile, delimiter=',')
            next(fileData)
            rows = sorted(fileData)
            return rows
    except FileNotFoundError:
        print("{} not found".format(file))
        quit()
