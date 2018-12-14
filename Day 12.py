from collections import deque
initial = '#.####...##..#....#####.##.......##.#..###.#####.###.##.###.###.#...#...##.#.##.#...#..#.##..##.#.##'
initial = deque([_ for _ in initial])
key = {}

with open('Inputs/Day 12.txt','r') as f:
    for i in f:
        i = i.strip()
        key[i[:5]] = i[-1]

genCount = 100 ## CHANGE TO 20 FOR PART 1
#Adding a few empty pots to the left for the early generations
for i in range(5):
    initial.appendleft('.')

for gen in range(genCount):
    nextGen = []
    for sides in range(3):
        #This is to add the unfilled pots on the right
        initial.append('.')

    length = len(initial)
    for i in range(length-2):
        pull = [initial[i-2],initial[i-1],initial[i],initial[i+1],initial[i+2]]    
        joinedPull = ''.join(pull)
        if joinedPull in key.keys():
            nextGen.append(key[joinedPull])
        else:
            nextGen.append('.')
    initial = deque([_ for _ in nextGen])

potSum = 0
for i,pot in enumerate(initial):
    if pot == '#':
        potSum += i
        potSum -= (5)
# The key evolves to a pattern of '...###...###...###',
# with every # shifting right each time.
# After enough generations, the growth is constant at 72 per generation
# So I run 100 generations and add (50bil - 100) * 72 at the end
potSum += (49999999900*72) ## COMMENT THIS OUT FOR PART 1

print(potSum)
