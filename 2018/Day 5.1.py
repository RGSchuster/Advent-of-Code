with open('Inputs\Day 5.txt','r') as f:
    rawList = list(f.read())

def compareLetters(a,b):
    if ((a.islower() and b.isupper()) or (a.isupper() and b.islower())) and \
       (a.upper() == b.upper()):
        return True

i = 0
while i < len(rawList) - 1:
    if compareLetters(rawList[i],rawList[i+1]):
        del rawList[i]
        del rawList[i]
        if i > 0:
                i -= 1
    else:
        i += 1

print(len(rawList))
