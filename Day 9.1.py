## Input: 476 players; last marble is worth 71431 points
numPlayers = 476
highMarb = 71431

scores = [0 for _ in range(numPlayers)]
board = [0]
curSpot = 0

for curMarble in range(1,highMarb+1):
    if curMarble % 23 == 0:
        curSpot -= 7
        curSpot %= len(board)
        scores[curMarble % numPlayers] += curMarble + board.pop(curSpot)
    else:
        if curSpot < len(board) - 1:
            curSpot = curSpot + 2
        elif curSpot == len(board) - 2:
            curSpot = len(board)
        else:
            curSpot = 1    
        board.insert(curSpot,curMarble)

print(scores.index(max(scores)),max(scores))
