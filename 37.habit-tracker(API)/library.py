import requests
from datetime import datetime

PIXELA_API = "https://pixe.la/v1/users"
USERNAME = "aslanthechessplayer"
GRAPH_ID = "***"
TOKEN = "***"
PIXELA_API_GRAPH = f"{PIXELA_API}/{USERNAME}/graphs"
PIXELA_GRAPH_1 = f"{PIXELA_API_GRAPH}/{GRAPH_ID}"


def register():
    param = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response = requests.post(url=PIXELA_API, json=param)
    if response.status_code == 200:
        print("Registration successful!")
    else:
        print(f"Registration failed. Error code: {response.status_code}")


def create_graph():
    param = {
        "id": "graph1",
        "name": "Chess Graph",
        "unit": "Hours",
        "type": "float",
        "color": "sora",
    }
    headers = {
        "X-USER-TOKEN": TOKEN,
    }
    response = requests.post(url=PIXELA_API_GRAPH, json=param, headers=headers)
    if response.status_code == 200:
        print("Graph creation successful!")
    else:
        print(f"Graph creation failed. Error code: {response.status_code}")


def add_delete_point(option: int):
    headers = {
        "X-USER-TOKEN": TOKEN,
    }
    if option == 0:
        while True:
            date = input("Enter the date for the new point (YYYYMMDD): ")
            try:
                datetime.strptime(date, '%Y%m%d')
                break
            except ValueError:
                print("Incorrect date format. Please enter in YYYYMMDD format.")
        hours = input("Enter the number of hours for the new point: ")
        param = {
            "date": date,
            "quantity": hours,
        }
        response = requests.post(url=PIXELA_GRAPH_1, json=param, headers=headers)
    elif option == 1:
        while True:
            date = input("Enter the date for the point to delete (YYYYMMDD): ")
            try:
                datetime.strptime(date, '%Y%m%d')
                break
            except ValueError:
                print("Incorrect date format. Please enter in YYYYMMDD format.")
        url = f"{PIXELA_GRAPH_1}/{date}"
        response = requests.delete(url=url, headers=headers)
