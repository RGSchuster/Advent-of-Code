import re
inputList = [[]]
spot = 0
with open('Inputs/Day 16.1.txt','r') as f:
    for row in f:
        if row.strip() == '':
            spot += 1
            inputList.append([])
        else:
            for i in re.findall(r'\d+',row):
                inputList[spot].append(int(i))

overallCount = 0
for i in inputList:
    count = 0
    before = [i[0],i[1],i[2],i[3]]
    A = i[5]
    B = i[6]
    C = i[7]
    after = [i[8],i[9],i[10],i[11]]

    # Addition
    if before[A] + before[B] == after[C]:
    ##    print('addr')
        count += 1
    if before[A] + B == after[C]:
    ##    print('addi')
        count += 1
    # Multiplication
    if before[A] * before[B] == after[C]:
    ##    print('mulr')
        count += 1
    if before[A] * B == after[C]:
    ##    print('muli')
        count += 1
    # Bitwise AND
    if before[A] & before[B] == after[C]:
    ##    print('banr')
        count += 1
    if before[A] & B == after[C]:
    ##    print('bani')
        count += 1
    # Bitwise OR
    if before[A] | before[B] == after[C]:
    ##    print('borr')
        count += 1
    if before[A] | B == after[C]:
    ##    print('bori')
        count += 1
    # Assignment
    if before[A] == after[C]:
    ##    print('setr')
        count += 1
    if A == after[C]:
    ##    print('seti')
        count += 1
    #Greater-than testing
    if (A > before[B] and after[C] == 1) or (A <= before[B] and after[C] == 0):
    ##    print('gtir')
        count += 1
    if (before[A] > B and after[C] == 1) or (before[A] <= B and after[C] == 0):
    ##    print('gtri')
        count += 1
    if (before[A] > before[B] and after[C] == 1) or (before[A] <= before[B] and after[C] == 0):
    ##    print('gtrr')
        count += 1
    # Equality testing
    if (A == before[B] and after[C] == 1) or (A != before[B] and after[C] == 0):
    ##    print('eqir')
        count += 1
    if (before[A] == B and after[C] == 1) or (before[A] != B and after[C] == 0):
    ##    print('eqri')
        count += 1
    if (before[A] == before[B] and after[C] == 1) or (before[A] != before[B] and after[C] == 0):
    ##    print('eqrr')
        count += 1
    
    if count >= 3:
        overallCount += 1

print('Overall Count:',overallCount)
