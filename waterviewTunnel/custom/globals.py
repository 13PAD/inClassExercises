import csv
filePath = None
errorPath = None
cars, errors = [], []
speedLimit = 80
fineRanges = [[0, 10], [11, 15], [16, 20], [21, 25],
              [26, 30], [31, 35], [36, 40], [41, 45]]
fines = [30, 80, 120, 170, 230, 300, 400, 510, 630]


def getFileData(file):
    with open(file) as csvfile:
        fileData = csv.reader(csvfile, delimiter=',')
        next(fileData)
        rows = sorted(fileData)
        csvfile.close()
        return rows


def getCustomFile():
    file = str(input('what is the filename?'))
    if file.lower() == 'exit':
        print('exiting')
        quit(1)
    try:
        myFile = open(file, 'r')
        myFile.close()
        return file
    except FileNotFoundError:
        print("that file is not found, check for correct name")
        return None


def getErrorFile():
    return input('what is the errorFile name?')
