from custom.tunnelDefs import *
from custom.globals import *
rows = getFileData(filePath)
rows = mergeDupes(rows)
length = changeLength()
cars = createCars(rows, length)
errors = checkForErrors(cars)
printOutputs(cars, errors)
