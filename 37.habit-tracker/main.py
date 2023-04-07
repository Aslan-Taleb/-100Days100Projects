from library import *
from art import *


def main():
    display_logo()
    register()
    create_graph()
    # Prompt the user to add or delete a point
    while True:
        choice = input("Enter 'add' to add a point or 'delete' to delete a point: ")
        if choice == "add":
            add_delete_point(0)
            break
        elif choice == "delete":
            add_delete_point(1)
            break
        else:
            print("Invalid choice. Please enter 'add' or 'delete'.")


if __name__ == "__main__":
    main()
