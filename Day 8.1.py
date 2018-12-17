with open('Inputs/Day 8.txt','r') as f:
    inputList = list(map(int,[_.split(' ') for _ in f.readlines()][0]))
#   
inputList = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
#   

answer = []

##def builder():
##    global inputList
##    global answer
##    children = inputList.pop(0)
##    metadata = inputList.pop(0)
##    for i in range(children + metadata):
##        answer.append([])
##    return first, second
##    
##while len(inputList) > 0:
##    first, second = builder()
##    if first > 0:
##        continue

childC = 0
metaC = 0

while len(inputList) > 0:
    first = inputList.pop(0)
    second = inputList.pop(0)
    if first == 0:
        print('yay')
    childC += first
    metaC += second
    

print(answer)
