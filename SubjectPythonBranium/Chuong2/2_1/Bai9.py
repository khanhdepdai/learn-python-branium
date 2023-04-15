#Check three float create right triangle
a,b,c = input("Enter a, b, c: ").split()
a = float(a)
b = float(b)
c = float(c)

#Check triangle

if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
    print("a,b,c can create right triangle!")
else:
    print("a,b,c don't create right triangle!")
