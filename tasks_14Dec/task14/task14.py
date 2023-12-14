# Task 14: Write a program that opens a file, writes "Hello, File!" to it, and closes the file.
def run():
    file_path = "file.txt"
    with open(file_path, 'w') as file:
        text = "Hello, File!"
        file.write(text)
        print(f"Skrev '{text}' til filen '{file_path}'")


if __name__ == "__main__":
    run()
