# https://birdeye.so/find-trades/

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch the browser
driver = webdriver.Chrome()  # Or use any other browser driver

# Navigate to the main page
driver.get('https://birdeye.so/')

# Wait for the iframe to be available
iframe_locator = (By.XPATH, "//iframe[contains(@id, 'cf-chl-widget')]")
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it(iframe_locator))

# Find the checkbox inside the iframe
checkbox_label_locator = (By.CLASS_NAME, "ctp-checkbox-label")
checkbox_label = WebDriverWait(driver, 15).until(EC.visibility_of_element_located(checkbox_label_locator))

# Find the checkbox input element within the label
checkbox_input_locator = (By.TAG_NAME, "input")
checkbox_input = checkbox_label.find_element(*checkbox_input_locator)

# Click the checkbox
checkbox_input.click()
