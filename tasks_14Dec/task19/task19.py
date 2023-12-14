# Task 19: Write a program that uses pickle to save and load a Python object.
import pickle

data = {"John": 25,
        "Benji": 12,
        "Alex": 19,
        "Patrick": 92
        }
file_path = "file.pickle"


def load_data():
    global data
    with open(file_path, "rb") as file:
        data = pickle.load(file)
    print(f"Data loaded from {file_path}")


def save_data():
    global data
    with open(file_path, "wb") as file:
        pickle.dump(data, file)
    print(f"Data saved to '{file_path}'")


def run():
    load_data()
    data["Henrik"] = 213
    print(data)
    save_data()


if __name__ == "__main__":
    run()
