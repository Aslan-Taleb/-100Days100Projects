from time import sleep

import selenium
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

USER = "aslantalebselim@gmail.com"
PASSWORD = "********"
LINK = "https://www.linkedin.com/jobs/search/?currentJobId=3536183273&f_AL=true&f_WT=2&geoId=105015875&keywords" \
       "=python%20developer&location=France&refresh=true"
PHONE = "0"


# CONFIGURATION
def config():
    path_driver = "C:\Program Files (x86)\ChromeDriver\chromedriver.exe"
    chrome_driver_path = path_driver
    service = Service(executable_path=chrome_driver_path)
    driver = WebDriver(service=service)
    driver.get(LINK)
    return driver


def save(driver):
    save = driver.find_element(By.CSS_SELECTOR, '.jobs-save-button')
    save.click()

"""
def apply(driver):
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()

        sleep(5)
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element_by_css_selector("footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()

            sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
        else:
            submit_button.click()

        sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()
    except NoSuchElementException:
        print("No application button, skipped.")

"""


def sign_in(driver):
    signup = driver.find_element(By.XPATH, '/html/body/div[5]/a[1]')
    signup.click()

    mail = driver.find_element(By.XPATH, '//*[@id="username"]')
    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    sign_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')

    mail.send_keys(USER)
    password.send_keys(PASSWORD)
    sign_button.click()
