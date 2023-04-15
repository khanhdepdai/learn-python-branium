import math


def is_prime(a):  # check prime number
    if a < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(a) + 1)):
            if a % i == 0:
                return False
        return True


def reverse_number(b):  # count reverse number
    reverse = 0
    while b != 0:
        reverse = b % 10 + reverse * 10
        b = b // 10
    return reverse


def is_reversible_number(a):  # check reversible number
    reverse = reverse_number(a)
    if reverse == a:
        return True
    else:
        return False


def reverse_is_prime(a):  # check reverse is prime
    reverse = reverse_number(a)
    if is_prime(reverse):
        return True
    else:
        return False


def sum_element(a):
    if a == 0:
        return 0
    else:
        return a % 10 + sum_element(a // 10)


def sum_element_is_prime(a):
    sum = sum_element(a)
    if is_prime(sum):
        return True
    else:
        return False


def list_prime(a, b):  # show list prime
    for i in range(a, b + 1):
        if is_prime(i):
            print(f"{i}", end=" ")
    print()

def list_reversible_number(a, b): # show list reversible number
    for i in range(a, b + 1):
        if is_reversible_number(i):
            print(f"{i}", end=" ")
    print()


def list_sum_element_is_prime(a, b): # show list sum element is prime
    for i in range(a, b + 1):
        if sum_element_is_prime(i):
            print(f"{i}", end=" ")
    print()


def is_perfect_square(n):
    if math.sqrt(n) - int(math.sqrt(n)) == 0:
        return True
    else:
        return False


def list_is_perfect_square(a, b):
    for i in range(a, b + 1):
        if is_perfect_square(i):
            print(f"{i}", end=" ")
    print()


str_a, str_b = input("Enter a, b:").split()
a = int(str_a)
b = int(str_b)
print("list prime number to a from b: ")
{list_prime(a, b)}
print("list reversible number to a from b: ")
{list_reversible_number(a, b)}
print("list perfect square to a from b: ")
{list_is_perfect_square(a, b)}
print("list sum is prime to a from b: ")
{list_sum_element_is_prime(a, b)}