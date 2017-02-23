#Problem 3: Largest Prime Factor
import math

n = 600851475143
l = []

for i in range(3,int(math.ceil(math.sqrt(n))), 2):
    while(n%i == 0):
        l.append(i)
        n=n/i;

if (n>2):
    l.append(n)

print (max(l))
