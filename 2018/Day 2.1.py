twoCount,threeCount = 0, 0
curRowCount = {}

with open('Inputs/Day 2.txt','r') as f:
    for row in f:
        for letter in row:
            curRowCount[letter] = curRowCount.get(letter,0) + 1
        if 2 in curRowCount.values(): twoCount += 1
        if 3 in curRowCount.values(): threeCount += 1
        curRowCount = {}
        
print(twoCount * threeCount)
