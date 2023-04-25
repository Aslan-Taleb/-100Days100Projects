from library import *


def main():
    print('↑↑↑↑ Used to Play the sounds ↑↑↑↑\n')
    print(LOGO)
    print("Welcome to the Morse code Translator!\n")
    display_menu()
    while True:
        direction = get_input("Choose an option (1, 2 or 3): ")
        if direction == "1":
            the_input = get_input("\nEnter the Text (or type 'quit' to exit): ")
            if the_input == "quit":
                print("\nGoodbye!")
                break
            result = encode(the_input.upper())
            print("Listen..👂")
            print(f"\nMorse Code: {result}\n")

            play_morse_code(result)
            pyperclip.copy(result)
            print("The output has been copied to the clipboard.\n")
        elif direction == "2":
            the_input = get_input("\nEnter the Morse code (or type 'quit' to exit): ")
            if the_input == "quit":
                print("\nGoodbye!")
                break
            result = decode(the_input)
            print(f"\nText: {result}\n")
            pyperclip.copy(result)
            print("The output has been copied to the clipboard.\n")
        elif direction == "3":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid input. Please choose option 1, 2 or 3.")
        display_menu()


if __name__ == '__main__':
    main()
