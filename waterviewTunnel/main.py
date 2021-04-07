from custom.tunnelDefs import *
from custom.globals import *
# importing custom files
while filePath is None:  # loop till valid file is given
    filePath = getDataFile()
errorPath = getOutputFile()  # get errorFile
rows = mergeDupes(getFileData(filePath))  # create the data
length = changeLength()  # change distance of tunnel
cars = createCars(rows, length)  # create instances of cars
problems = checkForErrors(cars, errors)  # check for errors
outputData(cars, problems, errorPath)  # prints and appends all data to files
