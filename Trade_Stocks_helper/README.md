# Stock and News Alert Bot

The Stock and News Alert Bot is a Python script that fetches the latest stock data for a specific company and sends SMS alerts when the stock price experiences significant changes. Additionally, it retrieves news articles related to the company and includes them in the alert message.

## Prerequisites

Before running this script, make sure you have Python installed on your computer. You'll also need the following:

- An Alpha Vantage API key for fetching stock data.
- A News API key for fetching news articles.
- A Twilio account for sending SMS alerts.

## Configuration

In the code, you need to configure the following:

- `STOCK`: The stock symbol of the company you want to monitor (e.g., "TSLA" for Tesla Inc).
- `COMPANY_NAME`: The name of the company for which you're monitoring the stock.
- `api_stock_key`: Your Alpha Vantage API key.
- `key_api`: Your News API key.
- Twilio authentication details (`account_sid` and `auth_token`).
- Twilio phone numbers for the sender (`from_`) and recipient (`to`) of SMS alerts.

## Usage

Run the script following the above steps.

The script will fetch the latest stock data for the specified company, calculate the percentage change, and retrieve news articles related to the company.

If the percentage change in the stock price is significant (greater than or equal to 5% or less than or equal to -5%), it will send an SMS alert containing the stock data and news headlines to the specified recipient.

You can customize the alert thresholds and recipient phone number as needed.

## Important Note

Ensure that you have valid API keys for Alpha Vantage and News API, as well as Twilio authentication details. Use this script responsibly and be mindful of API usage limits.