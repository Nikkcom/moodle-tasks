# Task 27: Write a program that measures the execution time of a loop using the “time” module.
import time


def run():
    start_time = time.time()
    num1 = 0
    for i in range(50000000):
        num1 += 1
    end_time = time.time()
    print(num1)
    print(f"time used: {end_time - start_time} seconds")


if __name__ == "__main__":
    run()
