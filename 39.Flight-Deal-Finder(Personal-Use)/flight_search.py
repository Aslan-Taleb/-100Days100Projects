from datetime import datetime, timedelta

import requests


# This class is responsible for talking to the Flight Search API.
class FlightSearch:
    def __init__(self, fly_from, fly_to):
        self.api_url = 'https://api.tequila.kiwi.com/v2/search'
        self.fly_from = fly_from
        self.fly_to = fly_to
        # Set up variables for API request
        self.date_from = ""  # TODAY
        self.date_to = ""  # +6 month
        self.api_key = "***"

    # Set up headers and parameters
    def search(self):
        self.get_date()
        headers = {'apikey': self.api_key}
        params = {
            'fly_from': self.fly_from,
            'fly_to': self.fly_to,
            'dateFrom': self.date_from,
            'dateTo': self.date_to}

        # Make request to Tequila Kiwi API
        response = requests.get(self.api_url, headers=headers, params=params)
        # Print response
        return response.json()

    def get_date(self):
        # Today's date
        today = datetime.now()
        # Tomorrow's date
        tomorrow = today + timedelta(days=1)
        # Date 6 months from today
        six_months_later = today + timedelta(days=6 * 30)
        # Format dates as strings
        self.date_from = tomorrow.strftime('%d/%m/%Y')
        self.date_to = six_months_later.strftime('%d/%m/%Y')
