a,b = input("Enter a,b in the ax + b = 0: ").split()
a = int(a)
b = int(b)
if a == 0 and b == 0:
    print("COUNTERLESS SOLUTION")
elif a == 0 and b != 0:
    print(" NO SOLUTION")
else:
    print(f" x = { - b / a}")