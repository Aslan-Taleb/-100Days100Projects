from ZillowScraper import *
from FormAdder import *


def main():
    print("Welcome to the Zillow to Google Form scraper and form filler!")
    print(
        "This program will scrape rental listings from Zillow, and automatically fill out a Google Form with the information.")
    print("Starting the scraping process now...")
    zillow = ZillowScraper()
    address = ZillowScraper().address
    prices = ZillowScraper().prices
    links = ZillowScraper().links
    print("Finished scraping rental listings from Zillow.")
    print("Starting the form filling process now...")
    adder = FormAdder(address, prices, links)
    print("Finished filling out the Google Form.")
    print("Program complete.")


if __name__ == "__main__":
    main()
