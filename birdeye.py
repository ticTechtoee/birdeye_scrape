# https://birdeye.so/find-trades/

import requests
from bs4 import BeautifulSoup

url = "https://birdeye.so/find-trades/"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the trade data
    trade_data = []
    trades = soup.find_all("div", class_="trade")
    for trade in trades:
        # Extract relevant information from each trade element
        # Adjust the code based on the structure of the website and the data you want to extract
        trade_info = {
            "title": trade.find("h2").text.strip(),
            "description": trade.find("p").text.strip(),
            # Add more fields as needed
        }
        trade_data.append(trade_info)

    # Print the extracted data
    for trade_info in trade_data:
        print(trade_info)
else:
    print("Failed to retrieve data from the website")