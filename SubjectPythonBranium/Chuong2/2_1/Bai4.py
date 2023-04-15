a,b,c = input("Enter 3 interger a,b,c: ").split()
a = int(a)
b = int(b)
c = int(c)

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

if a == b and a == c:
    print("NO RESULT")
else:
    max = a;
    if max < b:
        max = b
    if max < c:
        max = c
    print(f"max = {max}")