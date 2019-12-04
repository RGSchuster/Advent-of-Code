with open('Inputs/Day 21.txt','r') as f:
    inputList = [_.split() for _ in f]   

_, instructIndex = inputList.pop(0)
instructIndex = int(instructIndex)

for i,value in enumerate(inputList):
    inputList[i][1] = int(inputList[i][1])
    inputList[i][2] = int(inputList[i][2])
    inputList[i][3] = int(inputList[i][3])

lowestStep = [0,999999999]

for i in range(1):
    working = [i,0,0,0,0,0]
    instructNum = working[instructIndex]
    stepCount = 0

    while instructNum < len(inputList):
        opcode, A, B, C = inputList[instructNum]

        working[instructIndex] = instructNum
        
        if opcode == 'borr':
            working[C] = working[A] | working[B]
        elif opcode == 'addr':
            working[C] = working[A] + working[B]
        elif opcode == 'eqrr':
            if working[A] == working[B]:
                working[C] = 1
            else:
                working[C] = 0
        elif opcode == 'addi':
            working[C] = working[A] + B
        elif opcode == 'eqri':
            if working[A] == B:
                working[C] = 1
            else:
                working[C] = 0
        elif opcode == 'eqir':
            if A == working[B]:
                working[C] = 1
            else:
                working[C] = 0
        elif opcode == 'gtri':
            if working[A] > B:
                working[C] = 1
            else:
                working[C] = 0
        elif opcode == 'mulr':
            working[C] = working[A] * working[B]
        elif opcode == 'setr':
            working[C] = working[A]
        elif opcode == 'gtir':
            if A > working[B]:
                working[C] = 1
            else:
                working[C] = 0
        elif opcode == 'muli':
            working[C] = working[A] * B
        elif opcode == 'banr':
            working[C] = working[A] & working[B]
        elif opcode == 'seti':
            working[C] = A
        elif opcode == 'gtrr':
            if working[A] > working[B]:
                working[C] = 1
            else:
                working[C] = 0
        elif opcode == 'bani':
            working[C] = working[A] & B
        elif opcode == 'bori':
            working[C] = working[A] | B
        else:
            print('Unknown opcode:',opcode)
        
        instructNum = working[instructIndex] + 1
        stepCount += 1
        print(stepCount,working)
        if stepCount >= 10000000:
            break
    if stepCount < lowestStep[1]:
        lowestStep = [i,stepCount]
    print(lowestStep)
    
print(lowestStep)
