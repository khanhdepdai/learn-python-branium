def inputList():
    sets = []
    k = int(input("Enter k: "))
    for i in range(k):
        sets.insert(i, [int(x) for x in input(f"Enter test {i}").split()])
    return sets


def sumList(l):
    sum = 0
    for i in range(len(l)):
        if i % 2 == 0:
            sum += l[i]
    return sum


l = inputList()
for i in range(len(l)):
    print(f"Test {i + 1}: ")
    print(sumList(l[i]))