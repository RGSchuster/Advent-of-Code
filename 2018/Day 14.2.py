from collections import deque

cookbook = [3,7]

oneSpot = 0
twoSpot = 1

lookFor = '409551'

i = 0
while True:
    # Step 1: Add recipes
    newRecipe = cookbook[oneSpot] + cookbook[twoSpot]
    if newRecipe >= 10:
        cookbook.append(newRecipe//10)
        
    # Step 2: See if you found it
    temp = [str(_) for _ in cookbook[-len(lookFor):]]
    if ''.join(temp) == lookFor:
        print(len(cookbook) - len(temp))
        break

    # Repeat for second added recipe
    
    cookbook.append(newRecipe%10)

    temp = [str(_) for _ in cookbook[-len(lookFor):]]
    if ''.join(temp) == lookFor:
        print(len(cookbook) - len(temp))
        break
    
    # Step 3: Go to new recipe
    oneSpot += 1 + cookbook[oneSpot]
    oneSpot %= len(cookbook)
    twoSpot += 1 + cookbook[twoSpot]
    twoSpot %= len(cookbook)

    # Step 4: iterate i
    i += 1

##print(''.join(cookbook))
