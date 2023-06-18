from library import *
from art import *
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def main():
    print(logo)
    to_send = ""
    to_print, difference = get_stocks()
    to_send += f"{STOCK} : {to_print}\n"
    if difference >= 5 or difference <= -5:
        sms(to_send)
    else:
        print("no big deal 😁")
main()
