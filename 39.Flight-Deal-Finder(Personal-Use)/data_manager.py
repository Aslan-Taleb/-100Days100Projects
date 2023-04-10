import requests


class DataManager:
    def __init__(self, new_fly: tuple):
        self.new_fly = new_fly
        self.token = "***"

    def edit(self):
        # Define variables
        sheet_url_to_get = "https://api.sheety.co/52e4797d4ba4a030a600379c091918dd/flightDeals/prices"
        sheet_url_to_put = "https://api.sheety.co/52e4797d4ba4a030a600379c091918dd/flightDeals/prices"
        search_value = self.new_fly[0]

        # Set up headers with authentication
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

        # Fetch all rows
        response = requests.get(sheet_url_to_get, headers=headers)
        if response.status_code == 200:
            data = response.json()["prices"]
            for row in data:
                if row["city"].lower() == search_value.lower():
                    row_number = row["id"]
                    old_price = row["lowestPrice"]
                    city = row["city"]
                    print(f"City: {city}")
                    print(f"Old Lowest price: {old_price}")
                    print(f"New Lowest price: {self.new_fly[2]}")
                    if old_price <= self.new_fly[2]:
                        print("No update needed. The oldest price is better (or the same).")
                        return False
                    else:
                        # Define data to be updated
                        new_data = {
                            "iataCode": self.new_fly[1],
                            "lowestPrice": self.new_fly[2]
                        }

                        # Make PUT request to edit row
                        response = requests.put(f"{sheet_url_to_put}/{row_number}", headers=headers,
                                                json={"price": new_data})

                        # Check response
                        if response.status_code == 200:
                            print("Row updated successfully!")
                            print("Sending SMS...")
                            return True
                        else:
                            print(f"Error updating row: {response.text}")
                        break
            else:
                print(f"No row found with city '{search_value}'")
                return False
        else:
            print("Error fetching data from sheet")
            return False
