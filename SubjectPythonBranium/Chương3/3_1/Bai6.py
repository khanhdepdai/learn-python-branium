import math


def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True


def find_prime_number_next(n):
    prime_next = n + 1
    while is_prime(prime_next) == False:
        prime_next += 1
    return prime_next


def find_prime_number_previous(n):
    if n <= 2:
        return 'NOT AVAILABLE'
    else:
        if is_prime(n - 1):
            return n - 1
        else:
            return find_prime_number_previous(n - 1)


def factoring_into_primes_with_multiplication_sign(n):
    if n < 2:
       print("Invailid!")
    else:
        count = 0
        for i in range(2, n // 2 + 1):
            while n % i == 0:
                if count == 0:
                    print(f"{i}",end="")
                else:
                    print(f" * {i}",end="")
                n //= i
                count += 1

def factoring_into_primes_with_exponential_sign(n):
    if n < 2:
       print("Invailid!")
    else:
        count = 0
        for i in range(2, n // 2 + 1):
            count_exponential = 0
            check = False
            while n % i == 0:
                count_exponential += 1
                n //= i
                check = True
            if check:
                if count == 0:
                    print(f"{i}^{count_exponential}", end="")
                else:
                    print(f" * {i}^{count_exponential}",end="")
                count += 1


n = int(input("Enter n:"))
print(f"Find prime interger next of n: {find_prime_number_next(n)}")
print(f"Find prime interger previous of n: {find_prime_number_previous(n)}")
print("Factoring into primes with multiplication sign of n: ", end='')
factoring_into_primes_with_multiplication_sign(n)
print()
print("Factoring into primes with exponential sign of n: ", end='')
factoring_into_primes_with_exponential_sign(n)
