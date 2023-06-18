import smtplib
from datetime import datetime

import requests

MY_LAT = 45.828529
MY_LONG = 1.261750
UTC = 2


def get_time():
    now = datetime.now()
    hour = now.hour
    second = now.minute
    time = (hour, second)
    return time


def get_sun():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + UTC
    sunrise_minute = int(data["results"]["sunrise"].split("T")[1].split(":")[1]) + UTC
    sunrise = (sunrise_hour, sunrise_minute)
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + UTC
    sunset_Minute = int(data["results"]["sunset"].split("T")[1].split(":")[1]) + UTC
    sunset = (sunset_hour, sunset_Minute)
    return sunrise, sunset


def ISS_info():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return iss_latitude, iss_longitude


def is_it_near():
    pos_iss = ISS_info()
    if pos_iss[0] - 5 <= MY_LAT <= pos_iss[0] + 5 and pos_iss[1] - 5 <= MY_LONG <= pos_iss[1] + 5:
        print("It's Near i swear ! ")
        return True
    else:
        print("It's Not Near go sleep")
        return False


def is_it_dark():
    time = get_time()
    sunrise, sunset = get_sun()
    if sunrise < time < sunset:
        print("It's the Day ! ")
        return False
    else:
        print("It's the Night ! ")
        return True


def send_mail(message):
    my_email = "aslantalebselim@gmail.com"
    password = "tu_pense"
    # Connect to the SMTP server using a secure connection
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    connection = smtplib.SMTP(smtp_server, smtp_port)
    connection.starttls()
    # Login
    connection.login(user=my_email, password=password)
    # test email
    connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Look Up☝️\n\n{message}")
    connection.quit()
    print("i sent : " + message + "\n\n" + "to: " + my_email + "\n")
