import sys
isNum = False
factors = 0
enteredNum = 0


def checkNum(val):
    global newNumber
    try:
        newNumber = int(val)
        return True
    except ValueError:
        try:
            newNumber = float(val)
            return True
        except ValueError:
            return False


def fizz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 15
    elif num % 5 == 0:
        return 5
    elif num % 3 == 0:
        return 3
    else:
        return 0


while True:
    enteredNum = input('enter a number to check if is a factor of 3,5 or both or type stop to exit:\t')
    if enteredNum.lower() == 'stop':
        break
    isNum = checkNum(enteredNum)
    while not isNum:
        enteredNum = input('enter a number to check if is a factor of 3,5 or both:\t')
        isNum = checkNum(enteredNum)
    factors = fizz(newNumber)
    if factors == 15:
        print("%d is a factor of 15" % newNumber)
    elif factors == 5:
        print("%d is a factor of 5" % newNumber)
    elif factors == 3:
        print("%d is a factor of 3" % newNumber)
    else:
        print("%d is not a factor of 3 or 5" % newNumber)

print('ending the program...')
sys.exit()
