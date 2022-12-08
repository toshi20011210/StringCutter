inputString = """"""
addString = ""
tempArray = inputString.splitlines()

startTime = []
songName = []

i=0
for i in range (0, len(tempArray)):
    splittedTempArray = tempArray[i].split(" ", 1)
    startTime.append(splittedTempArray[0])
    songName.append(splittedTempArray[1])

startTime.append(addString)

print(startTime)
print(songName)
