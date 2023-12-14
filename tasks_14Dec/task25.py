# Task 25: Use the “random” module to generate a random number between 1 and 100.
import random


def run():
    r = random.randint(1, 100)

    print(f"Random number is {r}")


if __name__ == "__main__":
    run()
