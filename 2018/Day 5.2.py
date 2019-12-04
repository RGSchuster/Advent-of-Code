with open('Inputs\Day 5.txt','r') as f:
    rawList = list(f.read())

def compareLetters(a,b):
    if ((a.islower() and b.isupper()) or (a.isupper() and b.islower())) and \
       (a.upper() == b.upper()):
        return True

dedupeLetters = set(rawList)

minLength = 1e7

for letter in dedupeLetters:
    
    tempList = [x for x in rawList if x != letter.upper() and x != letter.lower()]
    i = 0
    while i < len(tempList) - 1:
        if compareLetters(tempList[i],tempList[i+1]):
            del tempList[i]
            del tempList[i]
            if i > 0:
                i -= 1
        else:
            i += 1  
    
    minLength = min(minLength,len(tempList))

print(minLength)
