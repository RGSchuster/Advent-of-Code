import re, operator
from collections import defaultdict

inputList = []
guards = {}
asleepMins = {}
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

guardSleepMinutesCounter = dict((i,{}) for i in list(guards.keys()))

for i, note in enumerate(inputList):
    curGuard = list(map(int,regex.findall(note)))[-1]
    if curGuard not in guardSleepMinutesCounter.keys():
        continue
    j = i+1
    while inputList[j][-2:] != 'ft' and j < endLoopValue:
        start = int(inputList[j][15:17])
        end = int(inputList[j+1][15:17])
        for minute in range(start,end):
            guardSleepMinutesCounter[curGuard][minute] = guardSleepMinutesCounter[curGuard].get(minute,0) + 1
        j += 2
maxMinute = [0,0,0] #Guard, Minute, Count

for guardId in guardSleepMinutesCounter.keys():
    sleepiestMinute,maxSleep = max(guardSleepMinutesCounter[guardId].items(), key=operator.itemgetter(1))
    if maxSleep > maxMinute[-1]:
        maxMinute = [guardId,sleepiestMinute,maxSleep]

print(maxMinute[0] * maxMinute[1])
