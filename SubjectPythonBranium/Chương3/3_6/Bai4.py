import math


def prime(n):
    if n < 2:
        return False
    else:
        for i in range(2,int(math.sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True


def input_List():
        sets = []
        n = int(input("Enter n: "))
        for i in range(n):
            sets.insert(i, [int(x) for x in input(f"Enter test {i + 1}: ").split()])
        return sets


sets = input_List()
check = False
for i in range(len(sets)):
    print(f"Test {i + 1}: ")
    for j in range(len(sets[i])):
        if prime(sets[i][j]):
            print(f"({j}, {sets[i][j]})", end=" ")
            check = True
    if check == False:
        print("Invalid")
    print()