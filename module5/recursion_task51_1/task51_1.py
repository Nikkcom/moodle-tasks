import os


def print_dir(current_path):
    print(current_path)

    for path, subdirs, files in os.walk(current_path):

        subdirs.sort()
        files.sort()

        for subdir in subdirs:

            next_path = os.path.join(current_path, subdir)

            if os.path.exists(next_path):
                print(next_path)
        for file in files:
            full_path = os.path.join(current_path, file)

            if os.path.exists(full_path):
                print(full_path)


def run():
    print("Paths...")
    print_dir(os.getcwd())
    print("Recursion...")


if __name__ == "__main__":
    run()
