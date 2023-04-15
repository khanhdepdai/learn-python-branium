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


n = int(input("Enter n:"))
print(f"n is prime number: {is_prime(n)}")
print(f"n is reversible number: {is_reversible_number(n)}")
print(f"reverse number of n is prime: {reverse_is_prime(n)}")
print(f"sum element is prime: {sum_element_is_prime(n)}")
