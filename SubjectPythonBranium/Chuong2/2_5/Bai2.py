import math
n = int(input("Enter total number of test:"))
count = n
while count > 0:
    str_a, str_b, str_k = input("Enter a, b, k: ").split()
    a = int(str_a)
    b = int(str_b)
    k = int(str_k)
    check = False #Check a -> b have or don't have prime?
    countPrime = 0;
    for i in range(a, b + 1, 1):
        checkPrime = False
        if i < 2:
            continue
        else:
            for j in range(2, i, 1):
                if i % j == 0:
                    checkPrime = True
                    break
            if checkPrime == False:
                print(f"{i}", end=" ")
                check = True
                countPrime += 1
        if countPrime == k:
            print()
            break

    if check == False:
        print("Not available")
    count = count - 1
else:
    print()
    print("complete!")