from collections import deque

with open('Inputs/Day 8.txt','r') as f:
    inputList = list(map(int,[_.split(' ') for _ in f.readlines()][0]))
#   
##inputList = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
#   

metaSum = 0
metaQ = deque([])
childQ = deque([])

# Start by pulling first header
childQ.append(inputList.pop(0))
metaQ.append(inputList.pop(0))

while True:
    # if the current child has children
    # then grab the header data
    if childQ[-1] != 0:
        childQ.append(inputList.pop(0))
        metaQ.append(inputList.pop(0))
            
    # if the current child has no children
    # then grab the number of metadata points based on last value in metaQ
    # and remove the last values from the queue (LIFO)
    # and, if there is a parent, reduce the expected number of children on the parent
    elif childQ[-1] == 0:
        for i in range(metaQ[-1]):
            metaSum += inputList.pop(0)
        metaQ.pop()   
        childQ.pop()
        if len(childQ) > 0:
            childQ[-1] -= 1
    # if current child has negative children
    # then exit loop
    else:
        print('You cannot have negative children')
        break
            
    # if the number of points you are looking for is the same as the number of points remaining
    # then add all the points and exit loop
    if len(inputList) == sum(childQ):
        metaSum += sum(childQ)
        break
    
print(metaSum)
