import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException,TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv
from selenium.webdriver.support.ui import WebDriverWait
loc="ayurvedic doctor in thoraipakkam" #input("Enter Location To Search : ")


driver= webdriver.Firefox()
#driver.get("https://www.google.com/maps/search/ayurvedic+doctor+in+perungudi/@13.0208721,80.1231215,13z/data=!3m1!4b1?entry=ttu")
driver.get(f"https://www.google.com/maps/search/{loc.strip().replace(' ' ,'+')}/@13.0208721,80.1231215,13z/data=!3m1!4b1?entry=ttu")
driver.implicitly_wait(30)
#full_list=[["NAME","TYPE","STATUS","RATING","PHONE NO.","ADDRESS","LINK"]]
eles2=[]
st=time.time()
while True:
    eles=driver.find_elements(By.CLASS_NAME,"hfpxzc")
    driver.execute_script("arguments[0].scrollIntoView();", eles[-1])
    if EC.visibility_of((By.XPATH,"//div[@class='PbZDve ']//p[@class='fontBodyMedium ']//span[@class='HlvSq']")) and EC.invisibility_of_element((By.XPATH,'//div[@class="lXJj5c Hk4XGb "]/div[@class="qjESne veYFef"]')):
        if driver.find_element(By.XPATH,"//div[@class='PbZDve ']//p[@class='fontBodyMedium ']//span[@class='HlvSq']").is_displayed():
            break
eles=driver.find_elements(By.CLASS_NAME,"hfpxzc")
print(eles[-1].get_attribute("aria-label"))

print([i.get_attribute("aria-label") for i in eles])

