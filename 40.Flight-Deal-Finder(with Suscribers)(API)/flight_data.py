from datetime import datetime


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, response):
        self.response = response

    def get_details(self):
        # Extract the relevant information
        i = 0
        lowest_price = float('inf')
        index = -1  # initialize index to -1
        for data in self.response['data']:
            price = int(data['price'])
            if price < lowest_price:
                lowest_price = price
                index = i
            i += 1

        # check if index is still -1, meaning there was no valid data
        if index == -1:
            return None, None

        departure_city = self.response['data'][index]['cityFrom']
        departure_airport = self.response['data'][index]['flyFrom']
        arrival_city = self.response['data'][index]['cityTo']
        arrival_airport = self.response['data'][index]['flyTo']
        link = self.response['data'][index]['deep_link']
        #we can make an google flight :
        #link = f"https://www.google.co.uk/flights?hl=en#flt={departure_airport}
        # .{arrival_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

        # Convert departure and arrival dates to datetime objects
        departure_date = datetime.strptime(self.response['data'][index]['route'][0]['local_departure'],
                                           '%Y-%m-%dT%H:%M:%S.%fZ')
        arrival_date = datetime.strptime(self.response['data'][index]['route'][-1]['local_arrival'],
                                         '%Y-%m-%dT%H:%M:%S.%fZ')

        # Calculate duration of flight in hours
        duration_seconds = (arrival_date - departure_date).total_seconds()
        duration_hours = duration_seconds / 3600
        # Print the extracted information
        mail = f"Low price alert! Only {lowest_price} dollars to fly from {departure_city}-{departure_airport} " \
              f"to {arrival_city}-{arrival_airport}, with a flight duration of {duration_hours:.2f} hours.\n{link}"
        the_data_for_sheet = arrival_city, arrival_airport, lowest_price
        try:
            return mail, the_data_for_sheet
        except KeyError:
            return None, None
