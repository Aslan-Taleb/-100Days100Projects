import requests
from bs4 import BeautifulSoup

date = "2000-08-12"


def get_top100(date):
    titles = []
    link = "https://www.billboard.com/charts/hot-100/"
    data_at_date = requests.get(f"{link}{date}")
    data_at_date = data_at_date.text
    soup = BeautifulSoup(data_at_date, "html.parser")
    result = soup.findAll('h3', class_='a-no-trucate')

    for i in result:
        titles.append(i.getText(strip=True))
    titles = [title.replace('\n', '').replace('\t', '') for title in titles]
    return titles


get_top100(date)
