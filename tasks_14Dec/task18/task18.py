# Task 18: Write a program that opens a file in r+ mode, reads its content, adds new content, and writes it back.
def run():
    file_path = "file.txt"
    with open(file_path, "r+") as file:
        existing_content = file.read()

        append_text = "\n" + "Text that were added to the file."
        print("Existing content:")
        print(existing_content)

        file.write(append_text)

        file.seek(0)

        modified_content = file.read()

        print("File now:")
        print(modified_content)


if __name__ == "__main__":
    run()
