# Using Part 1's code, I found working[2] to stabilize at 10551432
# so I need to find all divisors of 10551432 and sum them

divisors = [10551432]

for i in range(1,10551432//2 + 1):
    if 10551432 % i == 0:
        divisors.append(i)

print(sum(divisors))
