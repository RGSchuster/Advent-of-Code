with open('Inputs/Day 6.txt','r') as f:
    #Build list of ints with X,Y coordinates from text
    inputList = [[int(s) for s in row.strip().split(', ')] for row in f]
#
inputList = [[1, 1], [1, 6], [8, 3], [3, 4], [5, 5], [8, 9]]
#

#Build map
max_col, max_row = 0, 0
for col,row in inputList:
    max_col = max(max_col,col)
    max_row = max(max_row,row)

for i in range(max_col+2):
    for j in range(max_row+2):
        #adds 2 at end to include 0th row and final row
        grid = [[-1] * i for _ in range(j)]

#Fill map with raw data points
for num,node in enumerate(inputList):
    grid[node[1]][node[0]] = num

##function to find nearest point
def changePoint(A,R,B,L):
    #A = abovePoint
    #R = rightPoint
    #B = belowPoint
    #L = leftPoint
    cleanPoints = list(set([x for x in [A,R,B,L] if x != -1]))
    if len(cleanPoints) == 1:
        return cleanPoints[0]
    else:
        return -1

newGrid = []

#Fill rest of map with nearest point
changeMade = True
while changeMade == True:
    changeMade = False
    newGrid = grid.copy()
    for i in range(max_col):
        for j in range(max_row):
            if i == 0:
                belowPoint = grid[i+1][j]
                abovePoint = -1
            elif i == max_col - 1:
                belowPoint = -1
                abovePoint = grid[i-1][j]
            else:
                belowPoint = grid[i+1][j]
                abovePoint = grid[i-1][j]
            if j == 0:
                leftPoint = -1
                rightPoint = grid[i][j+1]
            elif j == max_row - 1:
                leftPoint = grid[i][j-1]
                rightPoint = -1
            else:
                leftPoint = grid[i][j-1]
                rightPoint = grid[i][j+1]
            nearest = changePoint(abovePoint,rightPoint,belowPoint,leftPoint)
            if nearest >= 0:
                newGrid[i][j] = nearest
                changeMade = True
                print(grid)
    grid = newGrid.copy()
print('DONE')
    

#Find largest area
