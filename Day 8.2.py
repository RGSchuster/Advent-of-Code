from collections import deque
import json

# I 'cheated' to build this input as a list of lists by adding file output in 8.1 code
with open('Inputs/Day 8.2.txt','r') as f:
    inputList = json.load(f)
#   
##inputList = [[10,11,12],[[99],2],1,1,2]
#   

metaSum = 0

def metaCounter(data):
    node = [_ for _ in data if type(_) is list]
    meta = [_ for _ in data if type(_) is int]
    global metaSum
    if len(node) == 0:
        metaSum += sum(meta)
    else:
        for i in meta:
            if i <= len(node):
                metaCounter(node[i-1])
            
metaCounter(inputList)

print(metaSum)
