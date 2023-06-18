from InternetSpeedTwitterBot import *

CHROME_DRIVER_PATH = 'C:\Program Files (x86)\ChromeDriver\chromedriver.exe'


def main():
    bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
    bot.get_internet_speed()
    bot.tweet_at_provider()


main()
