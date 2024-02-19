from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv
from selenium.webdriver.support.ui import WebDriverWait
import time
st=time.time()
loc="thoraipakkam"#input("Enter Location To Search For Ayurvedic Doctors: ")


driver= webdriver.Firefox()
#driver.get("https://www.google.com/maps/search/ayurvedic+doctor+in+perungudi/@13.0208721,80.1231215,13z/data=!3m1!4b1?entry=ttu")
driver.get(f"https://www.google.com/maps/search/ayurvedic+doctor+in+{loc}/@13.0208721,80.1231215,13z/data=!3m1!4b1?entry=ttu")
driver.implicitly_wait(10)
full_list=[["NAME","TYPE","STATUS","RATING","PHONE NO.","ADDRESS","LINK"]]

while True:
    eles=driver.find_elements(By.CLASS_NAME,"hfpxzc")
    driver.execute_script("arguments[0].scrollIntoView();", eles[-1])
    try:
        driver.execute_script("arguments[0].scrollIntoView();",driver.find_element(By.XPATH,"//div[@class='PbZDve ']//p[@class='fontBodyMedium ']//span[@class='HlvSq']"))
        eles=driver.find_elements(By.CLASS_NAME,"hfpxzc")
        break

    except NoSuchElementException:
        pass

    #if eles==psn and driver.find_element(By.XPATH,"//div[@class='PbZDve ']//p[@class='fontBodyMedium ']//span[@class='HlvSq']").text == "You've reached the end of the list.":
    '''try:
            element=WebDriverWait(driver,2).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='PbZDve ']//p[@class='fontBodyMedium ']//span[@class='HlvSq']")))
            eles=driver.find_elements(By.CLASS_NAME,"hfpxzc")

            break
        except Exception:
            pass'''
        
#psn=eles
print(eles[-1].get_attribute("aria-label"))
    
    

'''
for ele in eles:
    l=[]
    l.append(ele.get_attribute("aria-label").strip())#name
    print(ele.get_attribute("aria-label"))
#name
    
    for i in range(2):
        try:
            ele.click()
            ele.click()
            driver.execute_script("arguments[0].scrollIntoView();", ele)
            det1=WebDriverWait(driver,20).until(lambda driver: driver.find_element(By.CSS_SELECTOR,"div.RcCsl:nth-child(3) > button:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)").text.strip() !="")
            break
        except Exception:
            pass

    try:#type
        def typ():
            ty=driver.find_element(By.XPATH,'//button[@class="DkEaL "]')
            l.append(ty.text.strip())
        typ()
    except NoSuchElementException:
        l.append("Not Specified")
    except StaleElementReferenceException:
        typ()
#type
    try:#status
        def statu():
            stat=driver.find_element(By.XPATH,'//span[@class="ZDu9vd"]/span/span')
            status=stat.text.strip()
            if status == "Open" or status=="Closed" or status=="Closes soon":
                l.append("Functioning")
            else:
                l.append(status)
        statu()
    except NoSuchElementException:
        l.append("Not Specified")
    except StaleElementReferenceException:
        statu()
    #status()
    try:#rating
        def rat():
            rat=driver.find_element(By.XPATH,'//div[@class="F7nice "]/span/span[@aria-hidden="true"]')
            l.append(rat.text.strip())
        rat()
    except NoSuchElementException:
        l.append("Not Specified")
    except StaleElementReferenceException:
        rat()
    
    #rating()
    try:#phone                                   div.RcCsl:nth-child(4) > button:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)
        def phone():
            phn=driver.find_element(By.XPATH,'//button[@data-item-id="phone:tel:06381692647"]')
            l.append(phn.get_attribute("aria-label").replace("Phone: ","").strip())
        phone()
    except NoSuchElementException:
        l.append("Not Specified")
    except StaleElementReferenceException:
        phone()
    #phone()    
    add=driver.find_element(By.CSS_SELECTOR,'div.RcCsl:nth-child(3) > button:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)')
    l.append(add.text)#address
    
    #address()
    l.append(ele.get_attribute("href"))#link
    full_list.append(l)
    #link()

print(full_list)
et1=time.time()
print(st-et1)
with open(f"results_in_{loc}.csv",'w') as r:
#with open("G:\\PYTHON maps\\results\\test.csv",'w') as r:
    writer=csv.writer(r)
    writer.writerows(full_list)
r.close()
et2=time.time()
print(st-et2)'''