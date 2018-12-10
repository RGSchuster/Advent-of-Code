## Input: 476 players; last marble is worth 71431 points
from collections import deque
numPlayers = 476
highMarb = 71431*100

scores = [0 for _ in range(numPlayers)]
board = deque([0])

for curMarble in range(1,highMarb+1):
    if curMarble % 23 == 0:
        board.rotate(6)
        scores[curMarble % numPlayers] += curMarble + board.pop()
    else:
        board.rotate(-2)
        board.insert(0,curMarble)

print(scores.index(max(scores)),max(scores))
