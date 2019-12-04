import pandas as pd

with open('Inputs/Day 18.txt','r') as f:
    inputList = [_.strip() for _ in f]
    
nextMin = []
size = 10
emptyRow = ['$' for _ in range(size+1)]
nextMin.append(emptyRow)

for i in range(size):
    nextMin.append([])
    nextMin[i+1].append('$')
    for j in range(size):
        nextMin[i+1].append(inputList[i][j])
    nextMin[i].append('$')
nextMin[size].append('$')
nextMin.append(emptyRow)

inputList = pd.DataFrame(nextMin)
nextMin = pd.DataFrame([['$' for _ in range(size+2)] for _ in range(size+2)])

for i in range(size+2):
    for j in range(size+2):
        if inputList[i][j] == '$':
            continue
        print(inputList[i][j])




print(inputList)
print(nextMin)



# KEY
# . = open ground
# | = tree
# # = lumberyard
#
# . -> | if adj >= 3 of |, else .
# | -> # if adj >= 3 #, else |
# # -> # if adj >= 1 # and adj >= 1 |, else .
