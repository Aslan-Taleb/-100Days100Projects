# Internet Speed Twitter Bot

The Internet Speed Twitter Bot is a Python script that automates the process of checking your internet speed using Speedtest.net and complaining to your internet service provider (in this case, Algeria Telecom) on Twitter if the actual speed falls below the promised speed. The bot logs in to your Twitter account, performs a speed test, and tweets a complaint to your provider.

## Prerequisites

Before running this script, ensure you have Python installed on your computer. Additionally, you will need:

- Selenium WebDriver
- ChromeDriver (download and specify the path in the code)
- A valid Twitter account for login
- Internet speed promised by your provider (PROMISED_DOWN and PROMISED_UP in the code)

## Configuration

In the code, you need to configure the following:

- `TWITTER_EMAIL`: Your Twitter email or username.
- `TWITTER_PASSWORD`: Your Twitter password.
- `PROMISED_DOWN`: The promised download speed from your provider.
- `PROMISED_UP`: The promised upload speed from your provider.
- `CHROME_DRIVER_PATH`: The path to your ChromeDriver executable.

## Installation

1. Clone this repository to your local machine or download the ZIP file.

   ```bash
   git clone https://github.com/yourusername/internet-speed-twitter-bot.git

2.Install the required Python packages, including Selenium.

3.Make sure to download the ChromeDriver executable and specify its path in the code.

4.Run the script.

## Usage
Run the script following the above steps.

The script will perform a speed test on Speedtest.net and collect your download and upload speeds.

It will then log in to your Twitter account and compose a complaint tweet to your provider, mentioning the actual speeds and the promised speeds.

The tweet will be sent to your provider.

## Important Note
Please use this script responsibly and comply with Twitter's terms of service. Ensure that your complaint is valid and respectful.
