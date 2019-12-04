from collections import deque

cookbook = [3,7]

oneSpot = 0
twoSpot = 1

afterXrecipes = 409551
tenRecipes = []

for i in range(afterXrecipes + 10):
    # Step 1: Add recipes
    newRecipe = cookbook[oneSpot] + cookbook[twoSpot]
    if newRecipe >= 10:
        cookbook.append(newRecipe//10)
        if len(cookbook) > afterXrecipes:
            if newRecipe >= 10:
                tenRecipes.append(str(newRecipe//10))
            if len(tenRecipes) == 10:
                break
    cookbook.append(newRecipe%10)
    if len(cookbook) > afterXrecipes:
        tenRecipes.append(str(newRecipe%10))
        if len(tenRecipes) == 10:
            break
    # Step 2: Go to new recipe
    oneSpot += 1 + cookbook[oneSpot]
    oneSpot %= len(cookbook)
    twoSpot += 1 + cookbook[twoSpot]
    twoSpot %= len(cookbook)

print(''.join(tenRecipes))
