from rectangle import Rectangle
from rectangle_styles import DoubleLinesStyle, SingleLineStyle
import time


def run():
    rec1 = Rectangle(get_user_input("Skriv inn ønsket lengde på rektangel", True),
                     get_user_input("Skriv inn ønsket høyde"),
                     "",
                     DoubleLinesStyle())

    rec1.display()
    rec1.rectangle_style = SingleLineStyle()
    rec1.display()

    inpu = input("")


def get_user_input(message, numeric_bool=False):
    var = 0

    while True:

        print("-" * 30)
        print(message)

        user_input = input("")

        if not user_input.isdigit():

            if numeric_bool:
                print("Vennligst skriv et tall")
                time.sleep(1)
                continue
            else:
                return user_input[:1]

        user_input = int(user_input)

        if not 0 < user_input:
            print("Tall må være større enn 0")
            time.sleep(1)
            continue

        return user_input


if __name__ == "__main__":
    run()
