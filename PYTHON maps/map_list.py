from selenium import webdriver


from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


driver= webdriver.Firefox()

driver.get("https://www.google.com/maps/search/ayurvedic+doctor+in+perungudi/@13.0208721,80.1231215,13z/data=!3m1!4b1?entry=ttu")

full_list=[]
try:
    i=3
    while True:
        l1=[]
        ele=driver.find_element(By.XPATH,f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div{[i]}/div/a')
        l1.append(ele.get_attribute("aria-label"))#name
        ele.click()
        print("!!")
        time.sleep(5)
        print("!!!")
        ele1=driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[7]/div[3]/button/div/div[2]/div[1]')
        print("!!!")
        l1.append(ele1.text)#address
        print("!!!")
        try:
            ele2=driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[7]/div[4]/div[1]/div[2]/div/span[1]/span/span[1]')
            l1.append(ele2.text)#status
        except NoSuchElementException:
            l1.append("")#status
            print("Exception!")
        try:
            ele3=driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[7]/div[5]/button/div/div[2]/div[1]')
            ele3=driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[7]/div[4]/button/div/div[2]/div[1]')
            ele3=driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[7]/div[6]/button/div/div[2]/div[1]')

            l1.append(ele3.text)#
        except NoSuchElementException:
            print("Exception!!")
            l1.append("")
        l1.append(ele.get_attribute("href"))
        print("!!")

        full_list.append(l1)
        print("!")
        exit_ele=driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[1]/div/div/div[3]/span/button')
        exit_ele.click()
        
        scroll_end=driver.find_element(By.XPATH,f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div{[i]}/div/a')
        driver.execute_script("arguments[0].scrollIntoView();", scroll_end)
        
        time.sleep(5)
        
        i+=2
except NoSuchElementException:
    print("Eception!!!")
    pass

print(full_list)


