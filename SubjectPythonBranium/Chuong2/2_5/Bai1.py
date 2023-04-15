import math
n = int(input("Enter n:"))
check = False
if n < 2:
    check = True
else:
    for i in range(2,int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            check = True
            break

if check:
    print("n is not a prime")
else:
    print("n is prime")