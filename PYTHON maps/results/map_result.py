from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import csv
import time
loc=input("Enter Location To Search For Ayurvedic Doctors: ")
options = Options()
options.add_experimental_option("detach",True)

driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get(f"https://www.google.com/maps/search/ayurvedic+doctor+in+{loc}/@13.0208721,80.1231215,13z/data=!3m1!4b1?entry=ttu")

full_list=[["NAME","TYPE","STATUS","RATING","PHONE NO.","ADDRESS","LINK"]]

psn=[]
try:
    while True:
        eles=driver.find_elements(By.CLASS_NAME,"hfpxzc")
        driver.execute_script("arguments[0].scrollIntoView();", eles[len(eles)-1])
        
        if eles==psn:
            break
        psn=eles
        
except NoSuchElementException:
    pass


for ele in eles:
    l=[]
    l.append(ele.get_attribute("aria-label"))#name
    ele.click()
    time.sleep(5)
    
    try:#type
        ty=driver.find_element(By.XPATH,'//button[@class="DkEaL "]')
        l.append(ty.text)
    except NoSuchElementException:
        l.append("")
        
    try:#status
        stat=driver.find_element(By.XPATH,'//span[@class="ZDu9vd"]/span/span')
        l.append(stat.text) 
    except NoSuchElementException:
        l.append("")
    try:#rating
        rat=driver.find_element(By.XPATH,'//div[@class="F7nice "]/span/span[@aria-hidden="true"]')
        l.append(rat.text)
    except NoSuchElementException:
        l.append("")
    try:#phone
        phn=driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[7]/div[5]/button/div/div[2]/div[1]')
        l.append(phn.text)
    except NoSuchElementException:
        l.append("")
            
    add=driver.find_element(By.XPATH,'//div[@class="Io6YTe fontBodyMedium kR99db "]')
    l.append(add.text)#address
    
    clos=driver.find_element(By.XPATH ,'//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[1]/div/div/div[3]/span/button')
    clos.click()
    l.append(ele.get_attribute("href"))#link
    full_list.append(l)
    
print(full_list)
with open(f"G:\\PYTHON maps\\results\\results_in_{loc}.csv",'w') as r:
    writer=csv.writer(r)
    writer.writerows(full_list)
r.close()