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


driver= webdriver.Firefox()
#driver.get("https://www.google.com/maps/search/ayurvedic+doctor+in+perungudi/@13.0208721,80.1231215,13z/data=!3m1!4b1?entry=ttu")
driver.get(f"https://www.google.com/maps/search/{loc.strip().replace(' ' ,'+')}/@13.0208721,80.1231215,13z/data=!3m1!4b1?entry=ttu")
driver.implicitly_wait(30)
#full_list=[["NAME","TYPE","STATUS","RATING","PHONE NO.","ADDRESS","LINK"]]
eles2=[]
while True:
    eles=driver.find_elements(By.CLASS_NAME,"hfpxzc")
    driver.execute_script("arguments[0].scrollIntoView();", eles[-1])
    if EC.visibility_of((By.XPATH,"//div[@class='PbZDve ']//p[@class='fontBodyMedium ']//span[@class='HlvSq']")) and EC.invisibility_of_element((By.XPATH,'//div[@class="lXJj5c Hk4XGb "]/div[@class="qjESne veYFef"]')):
        if driver.find_element(By.XPATH,"//div[@class='PbZDve ']//p[@class='fontBodyMedium ']//span[@class='HlvSq']").is_displayed():
            break
n=0
while True:
    full_list=[["NAME","TYPE","STATUS","RATING","PHONE NO.","ADDRESS","LINK"]]
    del1= ""
    try:
        for ele in eles:
            l=[]
        #def name():
            l.append(ele.get_attribute("aria-label").strip())#name
            print(ele.get_attribute("aria-label"))
            
            driver.execute_script("arguments[0].scrollIntoView();", ele)
            
            ele.click() 
            ele.click()                                   
        #def click(driver):
            a="div.RcCsl:nth-child(3) > button:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)"
            
            det1=WebDriverWait(driver,30).until(EC.text_to_be_present_in_element_attribute((By.XPATH,'//button[@class="aoRNLd kn2E5e NMjTrf lvtCsd "]'),"aria-label",f'Photo of {ele.get_attribute("aria-label")}'))
            #print(driver.find_element(By.XPATH,'//h1[@class="DUwDvf lfPIob"]').text) 
        #def typ(driver):
            try:#type
                ty=driver.find_element(By.XPATH,'//button[@class="DkEaL "]')
                l.append(ty.text.strip())
            except NoSuchElementException:
                l.append("Not Specified")

        #def statu(driver):
            try:#status
                stat=driver.find_element(By.XPATH,'//div[@class="o0Svhf"]/span/span/span')
                status=stat.text.strip()
                if status == "Open" or status=="Closed" or status=="Closes soon":
                    l.append("Functioning")
                else:
                    l.append(status)
            except NoSuchElementException:
                l.append("Not Specified")
            
        #def rating(driver):
            try:#rating
                rat=driver.find_element(By.XPATH,'//div[@class="F7nice "]/span/span[@aria-hidden="true"]')
                l.append(rat.text.strip())
                
            except NoSuchElementException:
                l.append("Not Specified")
        
    #def phone(driver):
            try:#phone                                   div.RcCsl:nth-child(4) > button:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)
                phn=driver.find_element(By.XPATH,'//div[@class="RcCsl fVHpi w4vB1d NOE9ve M0S7ae AG25L "]//button[@data-tooltip="Copy phone number"]//div[@class="Io6YTe fontBodyMedium kR99db "]')
                l.append(phn.text.strip())
            except NoSuchElementException:
                l.append("No Specified")
            
        #def address(driver):
            
            add=driver.find_element(By.CSS_SELECTOR,a)
            l.append(add.text.strip())#address
        #def link():

            l.append(ele.get_attribute("href"))#link
            full_list.append(l)
            print(l)
            eles2.append(ele)
            n+=1
        with open(f"results_in_{loc}.csv",'w') as r:
            writer=csv.writer(r)
            writer.writerows(full_list)
        r.close()
        break
    except (StaleElementReferenceException,TimeoutException):
        eles=eles[:n+1]
        print("staled")

t2=time.time()
print((t2-st)/60)
#print(et2," ",(st-et2)/60)