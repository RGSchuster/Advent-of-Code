numbers = []
with open('01_input.txt','r') as f:
    for line in f:
        numbers.append(int(line[:-1]))

summ = 0
for number in numbers:
    summ = summ + ((number//3 - 2))

print(summ)
summ = 0
for number in numbers:
    numb = number
    while((numb//3 - 2)) > 0:
        summ = summ + ((numb//3 - 2))
        numb = numb//3 - 2

print(summ)
