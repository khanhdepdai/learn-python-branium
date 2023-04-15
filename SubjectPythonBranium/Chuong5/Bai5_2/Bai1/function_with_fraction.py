from Fraction import Fraction


def create_fraction():
    # This function create a new fraction
    str_numerator = input("Enter numerator: ")
    str_denominator = input("Enter denominator: ")
    numerator = int(str_numerator)
    denominator = int(str_denominator)
    while denominator == 0:
        str_denominator = input("Please retype!(denomination must engrave 0): ")
        denominator = int(str_denominator)
    new_fraction = Fraction()
    new_fraction.numerator = numerator
    new_fraction.denominator = denominator
    return new_fraction


def add_new_fraction_to_list(list_fraction: list):
    """This function create a new fraction and save a list"""
    new_fraction = create_fraction()
    list_fraction.append(new_fraction)


def show_fraction(fraction: Fraction):
    """This function show fraction to paramerter"""
    print(f"{fraction.numerator}/{fraction.denominator}")


def show_list_fraction(list_fraction: list):
    """This function show fractions in the list to parameter"""
    for i in range(len(list_fraction)):
        show_fraction(list_fraction[i])
        print()


def reduce_fraction_from_keyboard():
    """This function reduce fraction from keyboard"""
    new_fraction = create_fraction()
    new_fraction.reduce_fractions()
    return new_fraction


def sum_two_fraction_to_keyboard():
    """This function sum two fraction to keyboard"""
    new_fraction1 = create_fraction()
    new_fraction2 = create_fraction()
    sum_two_fraction = new_fraction1.sum(new_fraction2)
    sum_two_fraction.reduce_fractions()
    return sum_two_fraction


def subtract_two_fraction_to_keyboard():
    """This function subtract two fraction to keyboard"""
    new_fraction1 = create_fraction()
    new_fraction2 = create_fraction()
    subtract_two_fraction = new_fraction1.subtract(new_fraction2)
    subtract_two_fraction.reduce_fractions()
    return subtract_two_fraction


def multiple_two_fraction_to_keyboard():
    """This function subtract two fraction to keyboard"""
    new_fraction1 = create_fraction()
    new_fraction2 = create_fraction()
    multiple_two_fraction = new_fraction1.multiple(new_fraction2)
    multiple_two_fraction.reduce_fractions()
    return multiple_two_fraction


def divide_two_fraction_to_keyboard():
    """This function subtract two fraction to keyboard"""
    new_fraction1 = create_fraction()
    new_fraction2 = create_fraction()
    divide_two_fraction = new_fraction1.divide(new_fraction2)
    divide_two_fraction.reduce_fractions()
    return divide_two_fraction


def sum_total_fraction_to_list(list_fraction: list):
    """This function sum total fraction of list to parameter"""
    sum_fraction = Fraction(0, 1)
    for i in range(len(list_fraction)):
        sum_fraction = sum_fraction.sum(list_fraction[i])
    sum_fraction.reduce_fractions()
    return sum_fraction


def multiple_total_fraction_to_list(list_fraction: list):
    """This function sum total fraction of list to parameter"""
    mul_fraction = Fraction(1, 1)
    for i in range(len(list_fraction)):
        mul_fraction = mul_fraction.multiple(list_fraction[i])
    mul_fraction.reduce_fractions()
    return mul_fraction
