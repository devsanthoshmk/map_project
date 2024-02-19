from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time

# Set options for the Firefox profile
options = Options()
options.profile = webdriver.FirefoxProfile()

# Open Firefox browser with options
driver = webdriver.Firefox(options=options)

# Open a website
driver.get("https://www.example.com")

# Scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)  # Wait for 3 seconds

# Find an element by its class name and click it
element = driver.find_element_by_class_name("example-class")
element.click()

# Close the browser
driver.quit()
