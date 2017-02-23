#Problem 5: Smallest Multiple
import math

def genPrime():
    l = []
    isPrime = True
    j = 0

    l.append(2)

    for i in range(3, 20, 2):
        j = 0
        isPrime = True
        while(l[j]*l[j] <= i):
            if (i%l[j] == 0):
                isPrime = False
                break
            j+=1
        if (isPrime):
            l.append(i)

    return l

q = genPrime()
res = 1

for i in range(0, len(q)):
    a = int(math.floor(math.log(20) /math.log(q[i])))
    res = res * int(math.pow(q[i],a))

print res
