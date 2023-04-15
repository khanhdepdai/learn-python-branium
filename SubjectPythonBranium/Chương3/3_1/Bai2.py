def greatestCommonDivsor(a, b):
    if a < b:
        x = a
        a = b
        b = x
    if b == 0:
        return a
    else:
        return greatestCommonDivsor(b, a % b)

def leastCommonMultiple(a, b):
    lcm = a
    while lcm < a or lcm < b or lcm % a != 0 or lcm % b != 0:
        lcm = lcm + 1
    return lcm

str_a, str_b = input("Enter a, b: ").split()
a = int(str_a)
b = int(str_b)
print(f"Greatest common divsor: {greatestCommonDivsor(a,b)} ")
print(f"Least common multiple: {leastCommonMultiple(a,b)}")
