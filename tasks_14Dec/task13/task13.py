# Task 13: Write a program that opens a file, reads its content, and closes the file.
def run():
    file_path = "file.txt"

    try:
        with open(file_path, 'r') as file:

            file_content = file.read()
            print(file_content)

    except FileNotFoundError:
        print("Fant ikke filen!")


if __name__ == "__main__":
    run()
