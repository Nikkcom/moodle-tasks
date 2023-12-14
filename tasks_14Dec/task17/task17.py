# Task 17: Write a program that reads a file using readlines and prints each line.
def run():
    file_path = "file.txt"
    with open(file_path, "r") as file:
        file_content = file.readlines()
        for i in file_content:
            print(i.strip("\n"))


if __name__ == "__main__":
    run()
