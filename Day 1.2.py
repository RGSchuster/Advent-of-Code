inputList = []
frequency = 0
tracker = {0:True}
index = 0;

with open('Day 1.txt', 'r') as f:
    inputList = list(map(int, f.read().splitlines()))

while True:
    frequency += inputList[index]
    if frequency in tracker:
        print(frequency)
        break
    tracker[frequency] = True
    index += 1;
    if index == len(inputList):
        index = 0;
