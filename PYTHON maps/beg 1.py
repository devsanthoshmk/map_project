import time
st=time.time()
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException,TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv
from selenium.webdriver.support.ui import WebDriverWait
loc="ayurvedic doctor in thoraipakkam" #input("Enter Location To Search : ")


driver= webdriver.Firefox(headless=True)
#driver.get("https://www.google.com/maps/search/ayurvedic+doctor+in+perungudi/@13.0208721,80.1231215,13z/data=!3m1!4b1?entry=ttu")
driver.get(f"https://www.google.com/maps/place/Shree+Kriya+Ayurveda+And+Panchakarma+Vaidya+Sala/@12.939547,80.241639,17z/data=!3m1!4b1!4m6!3m5!1s0x3a525dd034c04aa5:0x924bfe1e543c98b6!8m2!3d12.939547!4d80.241639!16s%2Fg%2F11ns3tjjf8?authuser=0&hl=en&entry=ttu")
driver.implicitly_wait(30)
print(driver.find_element(By.CSS_SELECTOR,'div.RcCsl:nth-child(3) > button:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)').text)
driver.close()
st2=time.time()
print((st2-st)/60)