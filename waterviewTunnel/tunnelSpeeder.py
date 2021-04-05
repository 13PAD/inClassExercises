from custom.tunnelDefs import *
from custom.globals import *
while filePath is None:
    filePath = getCustomFile()
errorPath = getErrorFile()
rows = getFileData(filePath)
rows = mergeDupes(rows)
length = changeLength()
cars = createCars(rows, length)
problems = checkForErrors(cars)
outputData(cars, problems, errorPath)
