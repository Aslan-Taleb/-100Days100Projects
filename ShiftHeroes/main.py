from functions import *  
import time

def main():
    """
    Main function to manage reservation scheduling.
    """
    available_schedule = get_available()  # Get the currently available schedule
    print(f"Old schedule: {available_schedule}")

    new_schedule = available_schedule
    while new_schedule == available_schedule:
        new_schedule = get_available()  # Get the new available schedule
        time.sleep(2)  # Wait for 2 seconds before checking again
        print(f"New schedule: {new_schedule}")

    shifts = get_shifts(new_schedule)  # Get the available shifts
    booked_shifts = see_our_reservation(new_schedule)  # See our booked reservations
    post_reservation(shifts, booked_shifts)  # Make the reservation

if __name__ == "__main__":
    main()  # Call the main function if the script is executed as a standalone program