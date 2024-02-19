import time
st=time.time()
import multiprocessing
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException,TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv

def max_result():
    global driver
    loc="ayurvedic doctor in thoraipakkam" #input("Enter input(eg: gift shop in vandavasi) : ")#
    headOption = webdriver.FirefoxOptions()
    headOption.add_argument("--headless")
    driver = webdriver.Firefox(options=headOption)
    driver.get(f"https://www.google.com/maps/search/{loc.strip().replace(' ' ,'+')}/@13.0208721,80.1231215,13z/data=!3m1!4b1?entry=ttu" )
    #driver.implicitly_wait(30)
    while True:
        try:  
            eles=driver.find_elements(By.CLASS_NAME,"hfpxzc")
            driver.execute_script("arguments[0].scrollIntoView();", eles[-1])
            if EC.presence_of_element_located((By.XPATH,"//div[@class='PbZDve ']//p[@class='fontBodyMedium ']//span[@class='HlvSq']")) and EC.invisibility_of_element((By.XPATH,'//div[@class="lXJj5c Hk4XGb "]/div[@class="qjESne veYFef"]')):  
                if driver.find_element(By.XPATH,"//div[@class='PbZDve ']//p[@class='fontBodyMedium ']//span[@class='HlvSq']").is_displayed():
                    break
        except NoSuchElementException:
            continue


    eles=driver.find_elements(By.CLASS_NAME,"hfpxzc")
    full_list.append(eles)
with multiprocessing.Manager() as manager:
    full_list=manager.list([])
    for i in range(multiprocessing.cpu_count()):
        p=multiprocessing.Process(target=max_result)
        p.start()
    p.join()
    for i in range(multiprocessing.cpu_count()):
        p=multiprocessing.Process(target=max_result)
        p.start()
    p.join()
    print([len(ele) for ele in full_list])
t2=time.time()
print((t2-st)/60)