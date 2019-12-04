with open('Inputs/Day 19.txt','r') as f:
    inputList = [_.split() for _ in f]   

_, instructIndex = inputList.pop(0)
instructIndex = int(instructIndex)
working = [0,0,0,0,0,0] # Part 1
##working = [1,0,0,0,0,0] # Part 2
instructNum = working[instructIndex]

while instructNum < len(inputList):
    opcode, A, B, C = inputList[instructNum]
    A,B,C = int(A),int(B),int(C)

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
    
print(instructNum, working)
