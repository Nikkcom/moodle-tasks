# Task 4: Create a generator function that generates Fibonacci numbers indefinitely.
def run():
    fibgen = fib_gen()
    for i in range(20):
        print(next(fibgen))


def fib_gen():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    run()
