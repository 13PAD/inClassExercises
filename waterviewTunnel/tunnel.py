# Waterview tunnel program
from datetime import timedelta
import weakref

# Globals
myFile = open("tunnelTimes.csv", "r")
plates = []
instances = []
lengthOfTunnel = 2400
east = 185
west = 105


class Car:  # creating the object Car
    departure: object

    def __init__(self, name, entry):
        self.name = name
        self.entry = entry

    def __str__(self):
        return str(self.__class__) + '\n' + '\n'.join(
            ('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))

    def getExit(self, departure):
        self.departure = departure

    def speed(self):
        print("{} \t{}\t{}\t{}\t{:.2f}km/h".format(self.name, self.entry, self.departure, "duration", 0))


def checkIt(x):
    x: float or int  # gives the programs hints of what x could be
    try:
        x = int(x)
        return True
    except ValueError:
        try:
            x = float(x)
            return True
        except ValueError:
            print('wrong input try again')
            return False


def getDistance(side):
    isNum = False
    global distance
    while not isNum:
        distance = input("what is the distance away the %s camera is? press enter to leave as the default" % side)
        if distance == '':
            return None
        else:
            isNum = checkIt(distance)
    return distance


for line in sorted(myFile.readlines()):
    a = line.split(",")
    if a[0] not in instances:
        instanceName = a[0]
        instanceName = Car(a[0], a[1].strip("\n"))
        instances.append(str(instanceName))
    else:
        instanceName.getExit(a[1])


for instance in instances:
    print(instance)
    instance.speed()
# eastDistance = getDistance("east")
# westDistance = getDistance("west")



# for i in range(len(cars)):
#     print(cars[i])
#     for x in range(len(cars[i])):
#         className = Car(cars[i][0], cars[i][1], cars[i][2])
#         print("{} \t{}\t{}\t{}\t{:.2f}km/h".format(className.licence, className.entry, className.departure, "duration", 0))
