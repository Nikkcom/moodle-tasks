def run():
    for i in range(10):
        fibgen = fib_gen()
        print(next(fibgen))


def fib_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    run()
