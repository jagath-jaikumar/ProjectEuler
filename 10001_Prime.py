#Problem 7: 10001st prime

def isPrime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

i = 0
count = 0

while (count < 10001):
    if (isPrime(i)):
        count+=1
    i+=1

print(i-1)
