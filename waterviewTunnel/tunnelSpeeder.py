from custom.tunnelDefs import *
from custom.globals import *
while filePath is None:
    filePath = getDataFile()
errorPath = getOutputFile()
rows = mergeDupes(getFileData(filePath))
length = changeLength()
cars = createCars(rows, length)
problems = checkForErrors(cars, errors)
outputData(cars, problems, errorPath)
