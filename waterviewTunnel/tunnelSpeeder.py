from tunnelDefs import *
from globals import *
rows = getFileData(filePath)
rows = mergeDupes(rows)
cars = createCars(rows)
printOutputs(cars)
