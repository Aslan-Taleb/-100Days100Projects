import smtplib

import requests
from twilio.rest import Client


# This class is responsible for sending notifications with the deal flight details.
class NotificationManager:
    def __init__(self, message):
        self.message_to_send = message
        self.to_who = []
        self.token = "***"
        self.get_emails()

    def get_emails(self):
        sheet_url_to_get = "https://api.sheety.co/52e4797d4ba4a030a600379c091918dd/flightDeals/users"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        response = requests.get(sheet_url_to_get, headers=headers)
        if response.status_code == 200:
            data = response.json()['users']
            for row in data:
                self.to_who.append(row["email"].lower())

    def send_mail(self):
        my_email = "aslantalebselim@gmail.com"
        password = "tu_pense"
        # Connect to the SMTP server using a secure connection
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        connection = smtplib.SMTP(smtp_server, smtp_port)
        connection.starttls()
        connection.login(user=my_email, password=password)
        for customer in self.to_who:
            connection.sendmail(from_addr=my_email, to_addrs=customer,
                              msg=f"Subject:New Deal🦁️\n\n{self.message_to_send}")
            print("to: " + customer + "\n")
        print("i sent : " + self.message_to_send + "\n\n")
        connection.quit()
