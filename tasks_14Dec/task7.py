# Task 7: Write a function that takes an integer as input and uses an assert statement to check if it's positive.
def run():
    assert_function(10)
    assert_function(-3)
    assert_function(0.1)


def assert_function(num1):
    assert 0 < num1, "Number should be positive"

    print(f"Your number is {num1}")


if __name__ == "__main__":
    run()
