from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver

from art import *
import time

from selenium.webdriver.common.by import By

LINK = "http://orteil.dashnet.org/experiments/cookie/"
# CONFIGURATION
path_driver = "C:\Program Files (x86)\ChromeDriver\chromedriver.exe"
chrome_driver_path = path_driver
service = Service(executable_path=chrome_driver_path)
driver = WebDriver(service=service)
driver.get(LINK)


def main():
    print(logo)
    print("Welcome to the Cookie Clicker Bot!")
    print(
        "This bot will automatically click the cookie and purchase the most expensive upgrade that is currently "
        "affordable.")
    # Get cookie to click on.
    cookie = driver.find_element(By.ID, "cookie")

    # Get upgrade item ids.
    items = driver.find_elements(By.CSS_SELECTOR, "#store div")
    item_ids = [item.get_attribute("id") for item in items]

    timeout = time.time() + 1
    five_min = time.time() + 60 * 5  # 5minutes

    while True:
        cookie.click()
        # Every 5 seconds:
        if time.time() > timeout:

            # Get all upgrade <b> tags
            all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
            item_prices = []

            # Convert <b> text into an integer price.
            for price in all_prices:
                element_text = price.text
                if element_text != "":
                    cost = int(element_text.split("-")[1].strip().replace(",", ""))
                    item_prices.append(cost)

            # Create dictionary of store items and prices
            cookie_upgrades = {}
            for n in range(len(item_prices)):
                cookie_upgrades[item_prices[n]] = item_ids[n]

            # Get current cookie count
            money_element = driver.find_element(By.ID, "money").text
            if "," in money_element:
                money_element = money_element.replace(",", "")
            cookie_count = int(money_element)

            # Find upgrades that we can currently afford
            affordable_upgrades = {}
            for cost, id in cookie_upgrades.items():
                if cookie_count > cost:
                    affordable_upgrades[cost] = id

            # Purchase the most expensive affordable upgrade
            if affordable_upgrades:
                highest_price_affordable_upgrade = max(affordable_upgrades)
                to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

                driver.find_element(By.ID, to_purchase_id).click()
                print(f"Purchased upgrade with ID {to_purchase_id} for {highest_price_affordable_upgrade} cookies!")
            else:
                print("No affordable upgrades found.")

            # Add another 5 seconds until the next check
            timeout = time.time() + 5

        # After 5 minutes stop the bot and check the cookies per second count.
        if time.time() > five_min:
            cookie_per_s = driver.find_element(By.ID, "cps").text
            print(f"\nBot finished running. Cookies per second: {cookie_per_s}")
            break
main()