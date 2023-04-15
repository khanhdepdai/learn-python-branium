def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def miltiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return None
def exponential(a, b):
    return a ** b
def divideInterger(a, b):
    if b != 0:
        return a // b
    else:
        return None

str_a, str_b = input("Enter a, b:").split()

a = int(str_a)
b = int(str_b)

print(f"a + b = {add(a,b)}")
print(f"a - b = {subtract(a,b)}")
print(f"a * b = {miltiply(a,b)}")
print(f"a / b = {divide(a,b)}")
print(f"a^b = {exponential(a,b)}")
print(f"a // b = {divideInterger(a,b)}")