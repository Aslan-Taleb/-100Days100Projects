# ISS Location and Nighttime Checker

This Python script checks the International Space Station (ISS) location and determines whether it's near your location and whether it's currently nighttime. If both conditions are met, it sends an email notification.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python installed.
- Required Python packages installed (requests, smtplib).
- A Gmail account with [Less secure apps access](https://myaccount.google.com/lesssecureapps) enabled or an [App Password](https://support.google.com/accounts/answer/185833?hl=en) if you have two-factor authentication (2FA) enabled.

## Configuration

1. Replace `MY_LAT` and `MY_LONG` with your latitude and longitude coordinates.
2. Update the `my_email` and `password` variables with your Gmail email and password or app password.

## Usage

1. Run the script using Python:

   ```bash
   python iss_location_checker.py

The script will continuously check the ISS location and time conditions.

If the ISS is near your location and it's nighttime, it will send an email notification.

## Notes
    
The script checks if the ISS is within 5 degrees of your latitude and longitude.
It also checks if it's currently nighttime based on your local time and the sunrise/sunset times.

