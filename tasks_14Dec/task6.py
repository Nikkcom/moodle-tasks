# Task 6: Use a try statement to catch a ZeroDivisionError.
def run():
    print(divide(10, 2))
    print(divide(12, 3))
    print(divide(16, 0))


def divide(num1, num2):
    try:
        num3 = num1 // num2
    except ZeroDivisionError:
        print(f"Kan ikke dele {num1} på null!")
        return
    return num3


if __name__ == "__main__":
    run()
