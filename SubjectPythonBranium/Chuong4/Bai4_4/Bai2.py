s = input("Enter string: ").split()
b = set()
for i in s:
    if i in b:
        continue
    else:
        b.add(i)
        print(f'{i}: {s.count(i)}')

