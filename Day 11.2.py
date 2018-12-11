# Yay brute force
serial = 3613
gridSize = 301

def powerLevel(yC,xC):
    rack = xC + 10
    power = rack * yC
    power += serial
    power *= rack
    power = (power//100)%10
    power -= 5
    return power

a = [[_1 for _1 in range(gridSize)] for _2 in range(gridSize)]

for y in range(gridSize):
    for x in range(gridSize):
        a[y][x] = powerLevel(y+1,x+1)

largestPow = 0
curGrid = ['','','']
for y in range(gridSize):
    for x in range(gridSize):
        totalPow = a[y][x]
        for sqSize in range(1,(gridSize-1)):
            if x+sqSize >= (gridSize-1) or y+sqSize >= (gridSize-1):
                    continue
            for i in range(sqSize):
                totalPow += a[y+i][x+sqSize]
            for j in range(sqSize+1):
                totalPow += a[y+sqSize][x+j]
            if totalPow > largestPow:
                largestPow = totalPow
                curGrid = [x+1,y+1,sqSize+1]
                print(curGrid, largestPow)
    if y%10 == 0:
        print('y',y)
