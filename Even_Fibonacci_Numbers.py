# Problem 2: Even Fibonacci Numbers

prev = 1
curr = 2
sum = 0
while (curr < 4000000):
    if (curr % 2 == 0):
        sum += curr

    temp = curr
    curr = prev+curr
    prev = temp

print sum
