with open('Inputs/Day 25.txt','r') as f:
    inputList = [_.strip() for _ in f]

for i,value in enumerate(inputList):
    inputList[i] = tuple(map(int,value.split(',')))

def Distance(A,B):
    return abs(A[0]-B[0]) + abs(A[1]-B[1]) + abs(A[2]-B[2]) + abs(A[3]-B[3])

constsDict = [set() for _ in range(len(inputList))]

for const1 in range(len(inputList)):
    for const2 in range(len(inputList)):
        if Distance(inputList[const1],inputList[const2]) <= 3:
            constsDict[const1].add(const2)
            constsDict[const2].add(const1)

changeMade = True
while changeMade == True:
    changeMade = False
    for i in range(len(constsDict)):
        for value in constsDict[i]:
            if constsDict[i] == value:
                continue
            temp = set([_ for _ in constsDict[i]])
            constsDict[i] = set(list(constsDict[i]) + list(constsDict[value]))
            if constsDict[i] != temp:
                changeMade = True

distinct = []
for const in constsDict:
    if const not in distinct:
        distinct.append(const)

print(len(distinct))
