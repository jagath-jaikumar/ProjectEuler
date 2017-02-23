
product = 0
max = 0
for x in range(100,1000):
    for y in range(x,1000):
        product = x*y
        if (str(product) == str(product)[::-1]): 
            if (max < product):
                max = product
print max
