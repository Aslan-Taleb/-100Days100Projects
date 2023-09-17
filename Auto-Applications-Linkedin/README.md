# Job Search Bot

The Job Search Bot is a Python script that automates the process of searching for and saving job listings on LinkedIn. It uses Selenium to navigate the LinkedIn job search page, log in, and save job listings based on specified search criteria.

## Prerequisites

Before running this script, make sure you have the following installed:

- Python 3.x
- Selenium
- ChromeDriver (download and specify the path in the code)
- A LinkedIn account (used for logging in)

## Configuration

In the code, you need to configure the following:

- `path_driver`: Specify the path to your ChromeDriver executable.
- `JOB_TITLE`: The job title you want to search for on LinkedIn.
- `LOCATION`: The location for your job search.
- `MAIL_LINKEDIN`: Your LinkedIn email or username.
- `PASSWORD_LINKEDIN`: Your LinkedIn password.
- `PHONE`: Your phone number for job applications (optional).

## Installation

1. Clone this repository to your local machine or download the ZIP file.

2. Install the required Python packages, including Selenium.

3.Make sure to download the ChromeDriver executable and specify its path in the code.

4.Run the script.

## Usage

Run the script following the above steps.

The script will navigate to LinkedIn, log in using your credentials, and search for jobs based on your specified criteria.

It will then click on job listings and save them to your LinkedIn account.

The script will continue until all job listings on the page have been processed.

You can manually review the saved job listings on LinkedIn.