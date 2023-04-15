a,b = input("Enter two float a,b: ").split()
a = float(a)
b = float(b)

checkExit = bool(False)
print("Choose to 1 from 4: ")
print("1: Additional a with b")
print("2: Subtract a with b")
print("3: Multiply a with b")
print("4: Divide a with b")

choose = int(input())
match choose:
    case 1:
        print(f"a + b = {a + b}")
    case 2:
        print(f"a - b = {a - b}")
    case 3:
        print(f"a * b = {a * b}")
    case 4:
        if b == 0:
            print("Wrong!")
        else:
            print(f"a / b = {a / b}")
    case _:
        print(f"syntax wrong")