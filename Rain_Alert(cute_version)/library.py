import requests
import os
import random
from twilio.rest import Client


def sms(message_to_send):
    account_sid = '****'
    auth_token = '****'
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=message_to_send,
        from_='****',
        to='num_of_your_'
    )
    return message.status


def api_info():
    api_key = os.environ.get('')
    api_key = "****"
    LONG = -0.757970
    LATT = 35.739220
    link = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": LATT,
        "lon": LONG,
        "appid": api_key,
    }
    response = requests.get(link, params=params)
    response.raise_for_status()
    response = response.json()
    return response


def get_quotes_surnom():
    # Open the file containing the quotes
    with open("quotes.txt", "r") as f:
        # Read all lines from the file
        quotes = f.readlines()

    # Choose a random quote from the list of quotes
    chosen_quote = random.choice(quotes)

    # Remove the number and the dot from the beginning of the quote
    quote_parts = chosen_quote.split(". ", 1)
    if len(quote_parts) > 1:
        cleaned_quote = quote_parts[1]
    else:
        cleaned_quote = chosen_quote

    # Print the cleaned quote
    with open("surnom.txt", "r") as f:
        # Read all lines from the file
        nicknames = f.readlines()

    chosen_nickname = random.choice(nicknames)

    cleaned_nickname = chosen_nickname.strip()

    return cleaned_quote, cleaned_nickname


def is_it_gonna_rain(quotes, surnom):
    data = api_info()
    weather_id = data['weather'][0]['id']
    if weather_id < 700:
        status = sms(
            f"Point météo : Bring an umbrella ☂️\nQuotes of the day :{quotes}Bonne Journée {surnom}❤️ ")
        print( f"Point météo : Bring an umbrella ☂️\nQuotes of the day :{quotes}Bonne Journée {surnom}❤️ ")
    else:
        status = sms(
            f"Point météo :  it's ok it's ok 👕 \nQuotes of the day :{quotes}Bonne Journée {surnom}❤️ ")
    return status
