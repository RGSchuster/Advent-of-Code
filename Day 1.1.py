frequency = 0

with open('Day 1.txt', 'r') as f:
    for row in f:
        frequency += int(row)

print(frequency)
