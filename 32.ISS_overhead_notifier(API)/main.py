import requests
from config import *
import time


def main():
    message = "The ISS is above you in the sky."
    if is_it_near() and is_it_dark():
        send_mail(message)


while True:
    time.sleep(60)
    main()
