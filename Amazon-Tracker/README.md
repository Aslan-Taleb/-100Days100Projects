# Amazon Price Tracker

Amazon Price Tracker is a Python application that tracks the price of a product on Amazon and sends an email alert when the price reaches the desired amount.

## Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.x
- Requests
- Beautiful Soup 4
- The smtplib library (included in Python)

## Configuration

In the `library.py` file, you can customize the following settings:

- `LINK`: The URL of the Amazon product you want to track.
- `PRICE_WANTED`: The target price you want to achieve.

## Installation

1. Clone this repository to your local machine or download the ZIP file.
2.Run the application.

## Usage
Run the application following the above steps.

The application will automatically track the price of the specified product on Amazon.

If the price reaches or falls below the amount set in PRICE_WANTED, you will receive an email alert.
