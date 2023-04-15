l = []
m = int(input("Enter m: "))
n = int(input("Enter n: "))

for i in range(m):
    l.append([])
    for j in range(n):
        l[i].append(input(f'Enter element[{i}][{j}]: '))


for i in range(m):
    for j in range(n):
        print(l[i][j], end=' ')
    print()