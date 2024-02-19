from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Set the path to your Firefox profile
profile_path = "/home/santhosh/.mozilla/firefox/j8ngysh7.default"

# Create Firefox options and set the profile path
options = Options()
options.add_argument(f"--profile={profile_path}")

# Create a Firefox driver with the specified options
driver = webdriver.Firefox(options=options)

# Now you can use the 'driver' object for automation tasks
# For example, driver.get("https://www.example.com")

# Don't forget to close the driver when done
