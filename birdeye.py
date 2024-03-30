# https://birdeye.so/find-trades/

import requests
from bs4 import BeautifulSoup

url = "https://birdeye.so/find-trades/"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
cookies = {
    # Add cookies here
}
response = requests.get(url, headers=headers, cookies=cookies)

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
    print(f"Response Code: {response.status_code}")