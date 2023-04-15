def sum(l):
        sum = 0
        for i in range(len(l)):  # input each element of test
            sum += int(l[i])
        return sum
# input
str_k = input("Enter k number of test sets: ")
k = int(str_k)
sets = []
for i in range(k): # run each test of sets
    n = int(input(f"Enter number element of test {i + 1}: "))
    l = input(f"Enter element number {i + 1}: ").split()
    sets.insert(i,l)


# output
for i in range(k): # run each test of sets
    print(f"Test {i + 1}: ")
    print(sets[i])


# sum
for i in range(k): # run each test of sets
    print(f"Test {i + 1}: ")
    print(sum(sets[i]))