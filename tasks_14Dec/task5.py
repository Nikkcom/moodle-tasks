# Task 5: Write a program that handles a ValueError if the user enters a non-integer value.
def run():
    while True:
        print("Skriv inn et heltall")

        user_input = input("")

        try:
            user_input = int(user_input)
        except ValueError:
            print("Vennligst skriv inn et heltall!")
            continue


if __name__ == "__main__":
    run()
