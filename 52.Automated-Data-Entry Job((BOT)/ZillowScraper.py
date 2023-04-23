from time import sleep
import requests
import selenium
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver


class ZillowScraper:
    def __init__(self):
        self.link = 'https://www.zillow.com/homes/for_rent/'
        # self.driver = self.get_page()
        self.html = self.get_page()
        print("Get Information...")
        self.address, self.prices, self.links = self.get_information()

    def get_page_dont_work(self):
        #always robot verification who doesnt work
        path_driver = "C:\Program Files (x86)\ChromeDriver\chromedriver.exe"
        chrome_driver_path = path_driver
        service = Service(executable_path=chrome_driver_path)
        driver = WebDriver(service=service)
        driver.get(self.link)
        return driver

    def get_page(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/111.0.0.0 Safari/537.36",
            "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6",
        }
        try:
            response = requests.get(self.link, headers=headers)
        except requests.exceptions.MissingSchema:
            html = ""
        else:
            html = response.text
        return html

    def get_information(self):
        all_address = []
        all_prices = []
        all_links = []
        soup = BeautifulSoup(self.html, "html.parser")
        all_address_soup = soup.findAll('address')

        for address in all_address_soup:
            all_address.append(address.text)
        all_prices_soup = soup.findAll('span', {'data-test': 'property-card-price'})
        for price in all_prices_soup:
            reformat = price.text.split('+')[0]
            all_prices.append(reformat)
        all_links_soup = soup.findAll('a', {'data-test': 'property-card-link'})
        for link in all_links_soup:
            reformat = link.get('href')
            all_links.append('zillow.com' + reformat)
        return all_address, all_prices, all_links

