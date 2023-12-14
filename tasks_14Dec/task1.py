# Task 1: Write a program to print even numbers between 1 and 10 using a loop and continue statement.
def run():
    for i in range(10):
        i += 1
        if i % 2 != 0:
            continue
        print(i)


if __name__ == "__main__":
    run()
