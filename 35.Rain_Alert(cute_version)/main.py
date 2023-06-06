from library import *
from art import *
def main():
    print(logo)
    quote, name = get_quotes_surnom()
    status = is_it_gonna_rain(quote, name)
    print(status)

main()
