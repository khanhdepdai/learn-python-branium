#Check three float create triangle
a,b,c = input("Enter a, b, c: ").split()
a = float(a)
b = float(b)
c = float(c)

#Check triangle
if a + b > c and a + c > b and b + c > a:
    print("a,b,c create triangle!")
else:
    print("a,b,c don't create triangle!")

