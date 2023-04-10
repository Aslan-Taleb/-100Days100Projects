from flight_search import *
from flight_data import *
from data_manager import *
from notification_manager import *

CURRENT_POSITION = "TLS"
WHERE_TO_GO = ['ORN', 'RKV', 'HND']

# Affichage du message de bienvenue et du nom de l'application
print("=" * 50)
print("Bienvenue dans l'application Flight Deal Finder !")
print("=" * 50)


def main():
    notification_manager = NotificationManager("")
    for city in WHERE_TO_GO:
        flight_search_object = FlightSearch(CURRENT_POSITION, city)
        response = flight_search_object.search()
        flight_data = FlightData(response)
        the_sms, the_data = flight_data.get_details()
        data_manager = DataManager(the_data)
        sms_or_not = data_manager.edit()
        if sms_or_not:
            notification_manager.message_to_send = the_sms
            print("=" * 50)
            print(the_sms)
            print("=" * 50)
            # notification_manager.sms()
            # sms envoyé ! j'ai enlever mes identifiants car Github
    print("All flights have been checked.")


main()
