# Task 11: Use the Decimal module to perform precise arithmetic with two decimal numbers.
from decimal import *


def run():
    getcontext().prec = 5

    num1 = Decimal(5.323)
    num2 = Decimal(2.04)

    print(num1 + num2)
    print(num1 / num2)


if __name__ == "__main__":
    run()
