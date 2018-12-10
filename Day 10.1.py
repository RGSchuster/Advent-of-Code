import matplotlib.pyplot as plt
import re

with open('Inputs/Day 10.txt','r') as f:
    numbers = [re.findall(r'-?\d+',i) for i in f]

x, y, xV, yV = [],[],[],[]
for values in numbers:
    x.append(int(values[0]))
    y.append(int(values[1]))
    xV.append(int(values[2]))
    yV.append(int(values[3]))
    
#Example input: position=< 9,  1> velocity=< 0,  2>    
#Example output: [9, 1, 0 ,2]

for iteration in range(10000,10318):
    newX = []
    newY = []
    #move each point by i * it's directional velocity
    for i,xpoint in enumerate(x):
        newX.append(xpoint+(xV[i]*iteration))
    for i,ypoint in enumerate(y):
        newY.append(ypoint+(yV[i]*iteration))
    #lower the iteration mod in first half and reduce second half value
    #when I the grouping stops getting smaller and starts getting bigger again
    if iteration % 1 == 0 and iteration >= 10308:
        grid = plt.scatter(newX,newY,s=10)
        plt.savefig(str(iteration) + '.png')
