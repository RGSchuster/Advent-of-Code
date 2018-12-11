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
curGrid = ['','']
for y in range(gridSize-2):
    for x in range(gridSize-2):
        totalPow = a[y][x]   + a[y][x+1]   + a[y][x+2]   + \
                   a[y+1][x] + a[y+1][x+1] + a[y+1][x+2] + \
                   a[y+2][x] + a[y+2][x+1] + a[y+2][x+2]
        if totalPow > largestPow:
            largestPow = totalPow
            curGrid = [x+1,y+1]

print(curGrid)
