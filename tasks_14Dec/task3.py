def run():
    print(generate_square(2))
    print(generate_square(3))
    print(generate_square(4))
    print(generate_square(5))


def generate_square(number):
    if 1 <= number <= 5:
        return number ** 2
    raise ValueError


if __name__ == "__main__":
    run()
