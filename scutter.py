inputString = """"""
addString = ""
tempArray = inputString.splitlines()

startTime = []
songName = []

i=0
for i in range (0, len(tempArray)):
    splittedTempArray = tempArray[i].split(" ", 1)
    startTime.append(splittedTempArray[0])
    splittedSplittedTempArray = splittedTempArray[1].split("/", 1)
    songName.append(splittedSplittedTempArray[0])


startTime.append(addString)

print(startTime)
print(songName)
