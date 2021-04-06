import csv
filePath = None
errorPath = None
cars, errors = [], []
speedLimit = 80
fineRanges = [[0, 10], [11, 15], [16, 20], [21, 25],
              [26, 30], [31, 35], [36, 40], [41, 45]]
fines = [30, 80, 120, 170, 230, 300, 400, 510, 630]


def getDataFile():
    # get the user’s input for the data file name,
    # so that the user can choose a different
    # file to parse at the start of the program
    fileName = str(input('what is the filename? (type exit to exit)'))
    if fileName.lower() == 'exit':
        print('exiting')
        quit(1)
    try:
        myFile = open(fileName, 'r')
        myFile.close()
        return fileName
    except FileNotFoundError:
        print("that file is not found, check for correct name")
        return None


def getOutputFile():
    # gets the name so that the user can
    # have an output file of their choosing.
    return input('what is the errorFile name?')


def getFileData(file):
    # This is the main parsing function, as it is the function
    # that reads and gets the data from the file itself.
    with open(file) as csvfile:
        fileData = csv.reader(csvfile, delimiter=',')
        next(fileData)
        rows = sorted(fileData)
        csvfile.close()
        return rows
