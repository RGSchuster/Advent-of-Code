import re

claims = []
regex = re.compile('\d+')
thread = [[0]*1000 for _ in range(1000)]

with open('Day 3.txt','r') as f:
    for row in f:
##     [claim #, left_dist, top_dist, width, height]
        data = list(map(int,regex.findall(row)))
        claims.append(data)
        for row in range(data[2],data[2]+data[4]):
            for col in range(data[1],data[1]+data[3]):
                if thread[row][col] == 1:
                    thread[row][col] = 2
                elif thread[row][col] == 0:
                    thread[row][col] = 1

for claim in claims:
    overlapFound = False
    for row in range(claim[2],claim[2]+claim[4]):
        for col in range(claim[1],claim[1]+claim[3]):
            if thread[row][col] == 2:
                overlapFound = True
    if overlapFound == False:
        print('The claim with no overlaps is: ID #' + str(claim[0]))

