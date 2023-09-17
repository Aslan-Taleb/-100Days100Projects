from time import sleep
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


# CONFIGURATIO
def config(link):
    path_driver = ""
    chrome_driver_path = path_driver
    service = Service(executable_path=chrome_driver_path)
    driver = WebDriver(service=service)
    driver.get(link)
    return driver


def save(driver):
    save_button = driver.find_element(By.CSS_SELECTOR, '.jobs-save-button')
    save_button.click()


def apply(driver, phone):
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
        apply_button.click()

        sleep(5)
        phone = driver.find_element(By.TAG_NAME, "button")
        if phone.text == "":
            phone.send_keys(phone)

        next_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-button__text")
        next_button.click()
        sleep(1)
        review_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-button__text")
        review_button.click()
        submit_button = driver.find_element(By.CSS_SELECTOR, "artdeco-button__text")
        submit_button.click()
    except NoSuchElementException:
        print("No application button, skipped.")


def sign_in(driver, username, password):
    signup = driver.find_element(By.XPATH, '/html/body/div[5]/a[1]')
    signup.click()
    mail_text = driver.find_element(By.XPATH, '//*[@id="username"]')
    password_text = driver.find_element(By.XPATH, '//*[@id="password"]')
    sign_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')

    mail_text.send_keys(username)
    password_text.send_keys(password)
    sign_button.click()
