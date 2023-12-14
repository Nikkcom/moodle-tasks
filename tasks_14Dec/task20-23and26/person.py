# Task 20: Create a class called “Person” with attributes “name” and “age”.
# Task 21: Add a method to the “Person” class that prints a greeting.
# Task 23: Modify the “Person” class to handle a ValueError if the age is not an integer.
from decimal import Decimal


class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        try:
            self.age = Decimal(age)
        except ValueError:
            print("Value Error! Age is not a decimal number")
        self.count += 1

    def greet(self):
        print(f"{self.name}, {self.age}: Hello!")
