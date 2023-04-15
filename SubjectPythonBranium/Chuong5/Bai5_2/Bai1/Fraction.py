import math


def greatest_common_divisor(a, b):
    """This function return greatest common divisor"""
    if (a < b):
        c = a
        a = b
        b = c
    if (a % b == 0):
        return b
    else:
        return greatest_common_divisor(b, a % b)


class Fraction:
    """This class save fraction with behavior: sum, substract, multiple, divide, reduce fraction"""

    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def sum(self, fraction2: "Fraction") -> "Fraction":
        """Sum itself with other fraction """
        sum_fraction = Fraction()
        sum_fraction.numerator = self.numerator * fraction2.denominator + fraction2.numerator * self.denominator
        sum_fraction.denominator = self.denominator * fraction2.denominator
        return sum_fraction

    def subtract(self, fraction2: "Fraction") -> "Fraction":
        """Subtracat itself with other fraction """
        substract_fraction = Fraction()
        substract_fraction.numerator = self.numerator * fraction2.denominator - fraction2.numerator * self.denominator
        substract_fraction.denominator = self.denominator * fraction2.denominator
        return substract_fraction

    def multiple(self, fraction2: "Fraction") -> "Fraction":
        """Multiple itself with other fraction """
        multiple_fraction = Fraction()
        multiple_fraction.numerator = self.numerator * fraction2.numerator
        multiple_fraction.denominator = self.denominator * fraction2.denominator
        return multiple_fraction

    def divide(self, fraction2: "Fraction") -> "Fraction":
        """Divide itself with other fraction """
        divide_fraction = Fraction()
        divide_fraction.numerator = self.numerator * fraction2.denominator
        divide_fraction.denominator = self.denominator * fraction2.numerator
        return divide_fraction

    def reduce_fractions(self):
        """Reduce itself"""
        greatest_common = greatest_common_divisor(self.numerator, self.denominator)
        self.numerator //= greatest_common
        self.denominator //= greatest_common
