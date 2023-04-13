from library import *


def main():
    driver = config()
    sleep(5)
    sign_in(driver)
    sleep(2)  # Wait for more jobs to load

    # Click on all jobs on the page
    click_on_job = driver.find_elements(By.CSS_SELECTOR, '.job-card-container--clickable .flex-grow-1')
    i = 0
    for job in click_on_job:
        print(f"number of jobs : {i + 1} ")
        job.click()
        sleep(2)
        save(driver)
        i += 1
    print("over")
    input("")


main()
