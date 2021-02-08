
twelveHourTime = input("what is the time you want to convert, please use HH:MM:SS A/PM format  \n"
                           ":  ")
e = twelveHourTime.split()
currentTime = (e[0].split(":"))
timeAM_PM = (e[1])
currentHour = int(currentTime[0])
militaryHour = 0
militaryTime = []
if timeAM_PM == "AM":
    if currentHour == 12:
        militaryHour = 0
    else:
        militaryHour = currentHour
elif timeAM_PM == 'PM':
    if currentHour == 12:
        militaryHour = currentHour
    else:
        militaryHour = currentHour + 12
else :
    print('no')
militaryTime.append(str(militaryHour))
militaryTime.append(currentTime[1])
militaryTime.append(currentTime[2])

for i in range (len(militaryTime)-1):
    print(militaryTime[i],end=":")
print(militaryTime[2])
    

