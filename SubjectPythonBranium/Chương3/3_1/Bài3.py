def sumElement(n):
    if n < 0:
         n = n * (-1)
    if n < 10:
        return n
    else:
        return n % 10 + sumElement(n // 10)


def miltiplyElement(n):
    if n < 0:
        n = n * (-1)
    if n < 10:
        return n
    else:
        return (n % 10) * miltiplyElement(n // 10)
def firstElement(n):
    if n < 0:
         n = n * (-1)
    if n < 10:
        return n
    else:
        return firstElement(n // 10)

str_n = input("Enter n:")
n = int(str_n)
print(f"sum elements:{sumElement(n)}")
print(f"miltiply elements:{miltiplyElement(n)}")
print(f"first elements:{firstElement(n)}")