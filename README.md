# Stock Price Monitor

## Overview
This project aims to monitor the stock price of a specific company and send an email notification if the price decreases. It fetches real-time stock data from the Moneycontrol API and compares the current price with the previous one. If there's a decrease in price, an email alert is sent.

## Requirements
- Python 3.x
- requests library
- yagmail library

## Installation
1. Clone or download the repository to your local machine.
2. Install the required libraries using pip:
    ```
    pip install requests yagmail
    ```

## Usage
1. Run the `main.py` script.
2. Provide your email credentials as command-line arguments: `<password> <sender_email>`.
3. The script continuously checks the stock price of the specified company at regular intervals.
4. If the market is open and there's a decrease in price, an email notification is sent.

## Configuration
- Adjust the `CompanyName` and `URL` variables in the `get_data()` function to monitor the desired company's stock.
- Modify the email content and recipient in the `send_mail()` function according to your requirements.
- Ensure the correct API endpoint (`URL`) for fetching stock data.

## Notes
- The script currently monitors the stock price of "Vodafone Idea" listed on the NSE (National Stock Exchange).
- It uses a predefined API endpoint from Moneycontrol to fetch stock data. Ensure this endpoint is valid and up-to-date.
- The script assumes the stock data is in JSON format and follows a specific structure. Any changes in the API response may require modifications in the code.
