from datetime import *
from twilio.rest import Client

import requests

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


def get_stocks():
    api_stock_key = "***"
    parameters = {
        "function": 'FX_DAILY',
        "from_symbol": 'EUR',
        "to_symbol": 'USD',
        "apikey": api_stock_key,
    }
    response = requests.get(STOCK_ENDPOINT, parameters)
    response.raise_for_status()
    response = response.json()

    today = datetime.today().strftime('%Y-%m-%d')

    yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')

    today_data = float(response['Time Series FX (Daily)'][today]['4. close'])
    yesterday_data = float(response['Time Series FX (Daily)'][yesterday]['4. close'])
    print(f'Today ({today}): {today_data}')
    print(f'Yesterday ({yesterday}): {yesterday_data}')
    difference = round(((today_data - yesterday_data) / yesterday_data) * 100, 2)
    if difference < 0:
        difference = abs(difference)
        to_return = f"🔻 {difference}%"
        return to_return, difference
    else:
        to_return = f"🔺 {difference}%"
        return to_return, difference


# HINT 2: Work out the value of 5% of yesterday's closing stock price.

def get_news():
    article_title = []
    article_content = []
    key_api = "***"
    parameters = {
        "q": "tesla",
        "apiKey": key_api
    }
    response = requests.get(NEWS_ENDPOINT, parameters)
    response.raise_for_status()
    response = response.json()
    for i in range(0, 3):
        article_title.append(response['articles'][i]['title'])
        article_content.append(response['articles'][i]['description'])
    return article_title, article_content


def sms(message_to_send):
    account_sid = '*****'
    auth_token = '*****'
    client = Client(account_sid, auth_token)
    title, text = get_news()
    for i in range(0, len(title)):
        message_to_send += f"\nHeadline: {title[i]}"
        message_to_send += f"\nBrief:{text[i]}"
    message = client.messages \
        .create(
        body=message_to_send,
        from_='****',
        to='*****'
    )
    print(message_to_send)
