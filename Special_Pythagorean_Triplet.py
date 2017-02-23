#Problem 9: Special Pythagorean Triplet

for i in range(1, 500):
    for j in range(1,500):
        for k in range(1,500):
            if (i**2+j**2==k**2 and i+j+k == 1000):
                print i*j*k
