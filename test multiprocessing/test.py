from selenium import webdriver
from selenium.webdriver.common.by import By

loc="ayurvedic doctor in thoraipakkam" 
# headOption = webdriver.FirefoxOptions()
# headOption.add_argument("--headless")
driver = webdriver.Firefox()#options=headOption)
print("...")
driver.get(f"https://www.google.com")#/maps/search/{loc.strip().replace(' ' ,'+')}/@13.0208721,80.1231215,13z/data=!3m1!4b1?entry=ttu")
#driver.implicitly_wait(30)