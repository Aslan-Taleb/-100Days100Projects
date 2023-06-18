## Exercise Tracker : 

This is a Python program that helps you track your exercises and record them in a workout log. It uses the Nutritionix API to identify exercises based on user input, calculates the calories burned, and stores the exercise details in a Google Sheet.

## Prerequisites

To run this program, you need to have the following:

Python 3 installed on your machine

The required libraries installed:

requests (install with pip install requests)

datetime (should be available by default)

## Setup

Obtain the necessary credentials:

Obtain an API ID and API Key from Nutritionix.

Create a Google Sheet and obtain an API token from the Google Developers Console.

## Set up environment variables:

Set APP_ID, API_KEY, and TOKEN_SHEETY as environment variables, containing the respective values obtained in the previous step.

## Customize the program:

You can modify the GENDER, WEIGHT_KG, AGE, and HEIGHT_CM constants in the program to match your personal information.
Customize the text in the menu prompts and success messages according to your preference.