with open('Inputs/Day 8.txt','r') as f:
    inputList = list(map(int,[_.split(' ') for _ in f.readlines()][0]))
#   
inputList = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
#   

globalMeta = []

child = inputList.pop(0)
meta = inputList.pop(0)

def listBuilder(c,m):
    global globalMeta
    global inputList
##    if len(inputList) <= m:
##        return
    child = inputList.pop(0)
    meta = inputList.pop(0)
    for i in range(m):
        globalMeta.append(inputList.pop(-1))
    print(inputList)
    if child > 0:
        listBuilder(child,meta)

listBuilder(child,meta)


