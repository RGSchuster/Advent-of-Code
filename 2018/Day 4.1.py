import re, operator

inputList = []
guards = {}
regex = re.compile('\d+')

with open('Inputs/Day 4.txt','r',newline='\n') as f:
    for row in f:
        inputList.append(row[:-2])

inputList.sort()
# This puts the list into an order of:
# 1) Guard begins shift
# 2) falls asleep
# 3) wakes up
# Repeating 2&3 zero or more times

endLoopValue = len(inputList) - 2

for i, note in enumerate(inputList):
    if note[-2:] != 'ft': #Guard #### begins shift
        continue
    curGuard = (list(map(int,regex.findall(note))))[5]
    
    j = i+1
    while inputList[j][-2:] != 'ft' and j < endLoopValue:
        start = int(inputList[j][15:17])
        end = int(inputList[j+1][15:17])
        guards[curGuard] = guards.get(curGuard,0) + (end - start)
        j += 2

sleepiestGuard = max(guards.items(), key=operator.itemgetter(1))[0]

asleepMins = {}

for i, note in enumerate(inputList):
    if list(map(int,regex.findall(note)))[-1] != 2663:
        continue
    j = i+1
    while inputList[j][-2:] != 'ft' and j < endLoopValue:
        start = int(inputList[j][15:17])
        end = int(inputList[j+1][15:17])
        for minute in range(start,end):
            asleepMins[minute] = asleepMins.get(minute,0) + 1
        j += 2

sleepiestMinute = max(asleepMins.items(), key=operator.itemgetter(1))[0]
print(sleepiestGuard * sleepiestMinute)
