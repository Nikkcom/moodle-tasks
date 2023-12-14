# Task 16: Write a program that reads a file, prints the current position, seeks to the beginning, and reads the file
# again.
def run():
    file_path = "file.txt"
    with open(file_path, "r") as file:
        file_content = file.read()
        print(file_content)

        print(f"Cursor is at {file.tell()}")
        file.seek(0)


if __name__ == "__main__":
    run()
