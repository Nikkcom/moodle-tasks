# Task 2: Write a program to print numbers from 1 to 5 using a loop and break the loop when reaching 3.
def run():

    for i in range(5):
        i += 1
        print(i)
        if i == 3:
            break


if __name__ == "__main__":
    run()
