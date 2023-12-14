# Task 15: Write a program that creates a CSV file and adds a row of data to it.

import csv


def run():
    data = [
        ["John", 25, "Bergen"],
        ["Jack", 19, "Oslo"],
        ["Benji", 21, "Ålesund"]
    ]
    file_path = "file.csv"

    with open(file_path, 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)


if __name__ == "__main__":
    run()
