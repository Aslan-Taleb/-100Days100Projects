import requests
import json

# Replace this token with your actual API token
token = "***"
headers = {'Authorization': 'Bearer ' + token}

def get_available(type_planning="daily"):
    """
    Get a list of available planning IDs based on the specified planning type.

    Args:
        type_planning (str): The type of planning (e.g., "daily", "weekly").

    Returns:
        list: List of available planning IDs.
    """
    available_planning_ids = []
    url = f"https://shiftheroes.fr/api/v1/plannings?type={type_planning}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for row in data:
            if row['state'] == 'available':
                available_planning_ids.append(row['id'])
        return available_planning_ids
    else:
        return None

def get_shifts(planning_ids):
    """
    Get a dictionary of available shift IDs for each planning ID.

    Args:
        planning_ids (list): List of planning IDs.

    Returns:
        dict: Dictionary containing planning IDs as keys and lists of available shift IDs as values.
    """
    shifts_dict = {}

    for planning_id in planning_ids:
        available_shifts = []
        url = f"https://shiftheroes.fr/api/v1/plannings/{planning_id}/shifts"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            shifts_data = response.json()
            for shift in shifts_data:
                if shift['seats'] - shift['seats_taken'] > 0:
                    available_shifts.append(shift['id'])
        else:
            return None

        shifts_dict[planning_id] = available_shifts

    return shifts_dict

def see_our_reservation(planning_ids):
    """
    Get a list of shift IDs that we have already reserved for the given planning IDs.

    Args:
        planning_ids (list): List of planning IDs.

    Returns:
        list: List of reserved shift IDs.
    """
    reserved_shifts = []

    for planning_id in planning_ids:
        url = f"https://shiftheroes.fr/api/v1/plannings/{planning_id}/reservations"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            reservations_data = response.json()
            for reservation in reservations_data:
                reserved_shifts.append(reservation['shift_id'])
        else:
            return None

    return reserved_shifts

def post_reservation(shifts_dict, reserved_shifts):
    """
    Make reservations for available shifts that we have not already reserved.

    Args:
        shifts_dict (dict): Dictionary containing planning IDs as keys and lists of available shift IDs as values.
        reserved_shifts (list): List of reserved shift IDs.

    Returns:
        None
    """
    for planning_id, available_shifts in shifts_dict.items():
        for shift_id in available_shifts:
            if shift_id not in reserved_shifts:
                url = f"https://shiftheroes.fr/api/v1/plannings/{planning_id}/shifts/{shift_id}/reservations"
                response = requests.post(url, headers=headers)

                if response.status_code == 200:
                    print('Reservation created successfully.')
                else:
                    print("Error:", response.status_code)
