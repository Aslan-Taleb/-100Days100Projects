from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

link_form = "https://forms.gle/iXkFomzFEDhLgTaC8"


class FormAdder:
    def __init__(self, address, prices, links):
        self.link = link_form
        self.address = address
        self.prices = prices
        self.links = links
        self.driver = self.get_driver()
        self.get_page()

    def get_driver(self):
        path_driver = "C:\Program Files (x86)\ChromeDriver\chromedriver.exe"
        chrome_driver_path = path_driver
        service = Service(executable_path=chrome_driver_path)
        driver = WebDriver(service=service)
        return driver

    def get_page(self):
        driver = self.driver
        driver.get(self.link)
        sleep(3)
        i = 0
        #
        for i in range(0,len(self.prices)):
            address_fill = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div['
                                                         '2]/div/div[1]/div/div[1]/input')
            address_fill.send_keys(self.address[i])

            prices_fill = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div['
                                                        '2]/div/div[1]/div/div[1]/input')
            prices_fill.send_keys(self.prices[i])

            links_fill = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div['
                                                       '2]/div/div[1]/div/div[1]/input')
            links_fill.send_keys(self.links[i])
            send_button = driver.find_element(By.XPATH,
                                              '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            send_button.click()
            another_one_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            another_one_button.click()
