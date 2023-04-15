number1 = int(input("Enter number 1 interger: "))
number2 = int (input("Enter number 2 interger: "))
print(f"number 1 = {number1}")
print(f"number 2 = {number2}")
if number1 == number2:
    print("number 1 equal number 2")
else:
    x = number1 - number2
    if x < 0:
        x = x * - 1
    print(f"number 1 diffrent number 2 is {x}")
