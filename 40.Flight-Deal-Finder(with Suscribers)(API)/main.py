from flight_search import *
from flight_data import *
from data_manager import *
from notification_manager import *

CURRENT_POSITION = "TLS"
WHERE_TO_GO = ['DPS', 'ORN', 'RKV', 'HND']

# Affichage du message de bienvenue et du nom de l'application
print("=" * 50)
print("Bienvenue dans l'application 'AslaN Flight Deal Finder' !")
print("=" * 50)


def register_if_not():
    existing_account = input("Do you have an account with us? (y/n) ")
    if existing_account.lower() == 'y':
        print("cool ! lets search for the best deals...")
        pass
    else:
        first_name = input("Please enter your first name: ")
        last_name = input("Please enter your last name: ")
        email = input("Please enter your email address: ")
        email_confirmed = False
        while not email_confirmed:
            confirm_email = input(f"Confirm your email address ({email}): ")
            if confirm_email == email:
                email_confirmed = True
            else:
                print("Email addresses do not match. Please try again.")
        my_data = (first_name, last_name, email)
        my_object = DataManager(my_data)
        my_object.register()


def main():
    register_if_not()
    notification_manager = NotificationManager("")
    for city in WHERE_TO_GO:
        flight_search_object = FlightSearch(CURRENT_POSITION, city)
        try:
            response = flight_search_object.search()
            if response is None:
                raise ValueError("Response is None")
        except ValueError:
            pass
        else:
            flight_data = FlightData(response)
            the_mail, the_data = flight_data.get_details()
            data_manager = DataManager(the_data)
            mail_or_not = data_manager.edit()
            if mail_or_not:
                notification_manager.message_to_send = the_mail
                print("=" * 50)
                # notification_manager.send_mail()
                print("=" * 50)
                # notification_manager.send_mail()
                # mail envoyé ! j'ai enlevé mes identifiants car Github
    print("All flights have been checked.")


main()
