from library import *
from art import *

def main():
    print(logo)
    print("Welcome to the Amazon price tracker!")
    print("You can change the product link and target price in the library.py file.\n")
    html = get_amazon_page(LINK)
    print(html)
    if "Amazon" in html:
        product = get_information(html)
        message = i_send_or_not(product, PRICE_WANTED)
        if message is not None:
            send_mail(message)
    else:
        print(f"Invalid Amazon link: {LINK}")


main()
