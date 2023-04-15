a,b,c = input("Enter 3 interger a,b,c").split()
a = int(a)
b = int(b)
c = int(c)

if a == b and a == c:
    print("NO RESULT")
else:
    min = a
    if min > b:
        min = b
    if min > c:
        min = c
    print(f"min = {min}")