
from library import *
import re

JOB_TITLE = ''
LOCATION = ''
MAIL_LINKEDIN = ''
PASSWORD_LINKEDIN = ''
PHONE = ''

def main():
    print("******************************************************")
    print("*             Welcome to the Job Search Bot           *")
    print("******************************************************")

    link = f"https://www.linkedin.com/jobs/search/?keywords={JOB_TITLE}&location={LOCATION}"
    print(f"Searching for jobs with title '{JOB_TITLE}' in location '{LOCATION}'...")
    driver = config(link)
    sleep(5)
    sign_in(driver, MAIL_LINKEDIN, PASSWORD_LINKEDIN)
    print("Successfully logged in to LinkedIn.")
    sleep(5)  # Wait for more jobs to load

    # Click on all jobs on the page
    click_on_job = driver.find_elements(By.CSS_SELECTOR, '.job-card-container--clickable .flex-grow-1')
    i = 0
    for job in click_on_job:
        print(f"Number of jobs: {i + 1}")
        job.click()
        sleep(2)
        save(driver)
        i += 1
    print("Job search completed!")
    input("Press Enter to close the bot.")


if __name__ == '__main__':
    main()
