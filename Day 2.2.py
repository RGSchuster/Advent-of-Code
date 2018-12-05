inputList = []

with open('Inputs/Day 2.txt','r') as f:
    for row in f:
        inputList.append(row[:-1])

def compareWords():
    for i,baseWord in enumerate(inputList):
        for compareWord in range(i+1,len(inputList)):
            differCount = 0
            sameLetters = []
            for eachLetter in zip(baseWord,inputList[compareWord]):
                if eachLetter[0] != eachLetter[1]:
                    differCount += 1
                    if differCount == 2:
                        break
                else:
                    sameLetters.append(eachLetter[0])
            if differCount == 1:
                print(''.join(sameLetters))
                return

compareWords()
