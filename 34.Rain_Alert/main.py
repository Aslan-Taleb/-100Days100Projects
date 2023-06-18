import requests
import os
from twilio.rest import Client


def sms(message_to_send):
    account_sid = '*****'
    auth_token = '*****'
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=message_to_send,
        from_='****',
        to='*****'
    )
    return message.status


def api_info():
    api_key = "*****"
    LONG = 1.261750
    LATT = 45.833618
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


def is_it_gonna_rain():
    data = api_info()
    weather_id = data['weather'][0]['id']
    if weather_id < 700:
        response = sms("Bring an umbrella ☂️")
    else:
        response = sms("it's ok it's ok 👕")
    print(response)


def main():
    is_it_gonna_rain()


main()
