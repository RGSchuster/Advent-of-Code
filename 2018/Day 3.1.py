import re

regex = re.compile('\d+')
thread = [[0]*1000 for _ in range(1000)]
overlapCount = 0

with open('Day 3.txt','r') as f:
    for row in f:
##     [left_dist, top_dist, width, height]
        data = (list(map(int,regex.findall(row)[1:])))
        for row in range(data[1],data[1]+data[3]):
            for col in range(data[0],data[0]+data[2]):
                if thread[row][col] == 1:
                    thread[row][col] = 2
                    overlapCount += 1
                elif thread[row][col] == 0:
                    thread[row][col] = 1
                    
print(overlapCount)
