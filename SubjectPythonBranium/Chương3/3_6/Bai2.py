def sumElementInList(l):
        sum = 0
        for i in range(0, len(l)):
            sum += float(l[i])
        return sum


def inputList():
        k = int(input("Enter number of sets: "))
        #sets = []
        for i in range(k):
            sets.insert(i,input("Enter list number: ").split())
        return sets


sets = inputList()
for i in range(len(sets)):
    print(f"Test {i}: ")
    print(sumElementInList(sets[i]))