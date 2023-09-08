from library import *
from art import *


def main():
    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    date = input("Enter a date in YYYY-MM-DD format: ")
    while not date_pattern.match(date):
        print("Invalid date format. Please enter a date in YYYY-MM-DD format.")
        date = input("Enter a date in YYYY-MM-DD format: ")

    name = f"{date} Billboard 100"
    playlist_created = check_playlist(name)
    if playlist_created:
        print(f"\nPlaylist '{name}' already exists. Skipping playlist creation.")
        while True:
            choice = input("\nChoose an option:\n1. Enter a new date\n2. Quit\nChoice : ")
            if choice == "1":
                main()
                break
            elif choice == "2":
                print("Quitting...")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
    else:
        print(f"\nCreating playlist '{name}'...")
        create_playlist(name)
        print(f"\nRetrieving top songs at {date} from Billboard.com...")
        titles = get_top100(date)

        print(f"\nAdding songs to playlist '{name}'...")
        add_element_playlist(name, titles)

        print(f"\nPlaylist '{name}' created with {len(titles)} songs.")


print(logo)
main()
