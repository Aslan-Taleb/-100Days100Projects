## Birthday Wisher : 

This is a Python program that helps you manage birthdays and sends personalized birthday greetings via email. It reads a CSV file containing birthday information, checks if there are any birthdays today, picks a random letter template, replaces the placeholder with the person's name, and sends the customized letter to their email address.

## Prerequisites : 

To run this program, you need to have the following:

Python 3 installed on your machine

## Setup
Make sure you have the required libraries installed by running the following command:

pip install smtplib

pip install csv

Prepare the letter templates:

Create a directory named letter_templates.

Inside the letter_templates directory, create three text files named letter_1.txt, letter_2.txt, and letter_3.txt. Customize these files with your birthday greeting messages. Use the placeholder [NAME] to indicate where the person's name will be inserted.

Prepare the CSV file:

Create a CSV file named birthdays.csv.

Each row in the CSV file should contain the following columns: Name, Email, Year, Month, Day. Fill in the details of each person's birthday.

## Usage : 

The program will check if any birthdays match the current date (month and day). If there are any matches, it will select a random letter template, replace the [NAME] placeholder with the person's name, and send the customized letter to their email address.

Check the terminal output for messages indicating the birthdays and emails sent.

Note: Make sure your machine has an internet connection and that you have allowed access to less secure apps in your email account's security settings. For Gmail, you may need to enable "Allow less secure apps" or create an App Password for the program to send emails.