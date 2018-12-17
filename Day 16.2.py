# Run the proces from 16.1 and print anytime only 1 job is ran.
# Then comment out that job and run again.
# Repeat until all codes are identified.
# I have deleted that code (it can be found in Day 16.1.py) and just left my findings
# These are in the order I identified them:

# 10 = muli
# 3 = addi
# 7 = mulr
# 1 = addr
# 0 = borr
# 15 = bori
# 12 = seti
# 9 = gtir
# 8 = setr
# 11 = banr
# 14 = bani
# 4 = eqri
# 2 = eqrr
# 6 = gtri
# 13 = gtrr
# 5 = eqir

inputList = []
with open('Inputs/Day 16.2.txt','r') as f:
    for row in f:
        row = row.split()
        row = list(map(int,row))
        inputList.append(row)
        
working = [0,0,0,0]

for i in inputList:    
    opcode, A, B, C = i
    
    if opcode == 0: # borr
        working[C] = working[A] | working[B]
    elif opcode == 1: # addr
        working[C] = working[A] + working[B]
    elif opcode == 2: # eqrr
        if working[A] == working[B]:
            working[C] = 1
        else:
            working[C] = 0
    elif opcode == 3: # addi
        working[C] = working[A] + B
    elif opcode == 4: # eqri
        if working[A] == B:
            working[C] = 1
        else:
            working[C] = 0
    elif opcode == 5: # eqir
        if A == working[B]:
            working[C] = 1
        else:
            working[C] = 0
    elif opcode == 6: # gtri
        if working[A] > B:
            working[C] = 1
        else:
            working[C] = 0
    elif opcode == 7: # mulr
        working[C] = working[A] * working[B]
    elif opcode == 8: # setr
        working[C] = working[A]
    elif opcode == 9: # gtir
        if A > working[B]:
            working[C] = 1
        else:
            working[C] = 0
    elif opcode == 10: # muli
        working[C] = working[A] * B
    elif opcode == 11: # banr
        working[C] = working[A] & working[B]
    elif opcode == 12: # seti
        working[C] = A
    elif opcode == 13: # gtrr
        if working[A] > working[B]:
            working[C] = 1
        else:
            working[C] = 0
    elif opcode == 14: # bani
        working[C] = working[A] & B
    elif opcode == 15: # bori
        working[C] = working[A] | B
    else:
        print('Unknown opcode:',opcode)

print(working,i)
