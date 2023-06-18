import requests

parameters = {
    "amount": 25,
    "type": "boolean",
    "category": "18"

}
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()
