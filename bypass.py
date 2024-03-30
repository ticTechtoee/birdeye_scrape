import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch the browser
driver = webdriver.Chrome()  # Or use any other browser driver

# Navigate to the website
driver.get("https://birdeye.so/find-trades/")

# Wait for the checkbox to be clickable
# Wait for the checkbox to be clickable with a longer timeout
checkbox = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']")))

# Click the checkbox
checkbox.click()

# Wait for the page to load after clicking the checkbox
time.sleep(5)  # Adjust the time as needed

# Extract the trade data using Selenium
trade_data = []
trades = driver.find_elements(By.CLASS_NAME, "trade")
for trade in trades:
    trade_info = {
        "title": trade.find_element(By.TAG_NAME, "h2").text.strip(),
        "description": trade.find_element(By.TAG_NAME, "p").text.strip(),
        # Add more fields as needed
    }
    trade_data.append(trade_info)

# Print the extracted data
for trade_info in trade_data:
    print(trade_info)

# Close the browser
driver.quit()
