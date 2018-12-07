with open('Inputs\Day 7.txt','r') as f:
    inputList = [_ for _ in f]

inputList = ['Step C must be finished before step A can begin.',
'Step C must be finished before step F can begin.','Step A must be finished before step B can begin.',
'Step A must be finished before step D can begin.','Step B must be finished before step E can begin.',
'Step D must be finished before step E can begin.','Step F must be finished before step E can begin.']

lines = [x.split() for x in inputList]
rules = [[line[1],line[7]] for line in lines]
# ['C', 'A'] = C must be finished before A can start

before = [_[0] for _ in rules]
after = [_[1] for _ in rules]
   
##print('Before:',before)
##print('After:',after)

ordering = {}
for i,letter in enumerate(after):
    if letter not in ordering.keys():
        ordering[letter] = [before[i]]
    else:
        ordering[letter].append(before[i])
    ordering[letter].sort()
#'E': ['B', 'D', 'F'] = B, D, and F must be finished before E can start

start = [x for x in set(before) if x not in set(after)]

answer = [min(start)]
workingLetters = []

for i in start:
    if i == min(start):
        continue
    workingLetters.append(i)

#list.remove(item)
i = 0

while len(answer) < len(set(before)|set(after)):
    curLetter = answer[i]
    #go thru every key and see if the current letter is in the value list
    #delete it if true
    #if the length of the key's new value is 0, put the key into workingLetters and delete it
    for key in ordering.keys():
        if curLetter in ordering[key]:
            ordering[key].remove(curLetter)
            if len(ordering[key]) == 0:
                workingLetters.append(key)
    for j in workingLetters:
        if j in ordering.keys():
            ordering.pop(j, None)
    if len(workingLetters) > 0:
        answer.append(min(workingLetters))
        i += 1
        workingLetters.remove(answer[i])
    print(workingLetters)

print(''.join(answer))










        
