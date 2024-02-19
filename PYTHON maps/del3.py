import time
st=time.time()
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException,TimeoutException

loc = "thoraipakkam"

driver = webdriver.Firefox()
driver.get(f"https://www.google.com/maps/search/ayurvedic+doctor+in+{loc}/@13.0208721,80.1231215,13z/data=!3m1!4b1?entry=ttu")
driver.implicitly_wait(30)

# Use WebDriverWait for elements to load
wait = WebDriverWait(driver, 20)
while True:
    eles=driver.find_elements(By.CLASS_NAME,"hfpxzc")
    driver.execute_script("arguments[0].scrollIntoView();", eles[-1])
    try:
        driver.execute_script("arguments[0].scrollIntoView();",driver.find_element(By.XPATH,"//div[@class='PbZDve ']//p[@class='fontBodyMedium ']//span[@class='HlvSq']"))
        eles=driver.find_elements(By.CLASS_NAME,"hfpxzc")
        break

    except NoSuchElementException:
        pass
# Move repeated code outside the loop

def click_element(element):
    element.click()
    element.click()  # Double-click

while True:
    try:
        full_list = [["NAME", "TYPE", "STATUS", "RATING", "PHONE NO.", "ADDRESS", "LINK"]]
        del1 = ""

        for ele in eles:
            l = []

            l.append(ele.get_attribute("aria-label").strip())  # name

            # Use Selenium methods to interact with elements
            click_element(ele)

            # Use WebDriverWait for dynamic content\
            
            while driver.find_element(By.CSS_SELECTOR, 'div.RcCsl:nth-child(3) > button:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)').text.strip() == del1:
                click_element(ele)
                time.sleep(0.5)
            del1 = driver.find_element(By.CSS_SELECTOR, 'div.RcCsl:nth-child(3) > button:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)').text.strip()
            
            l.append(driver.find_element(By.XPATH, '//button[@class="DkEaL "]').text.strip() if driver.find_elements(By.XPATH, '//button[@class="DkEaL "]') else "Not Specified")  # type

            status = driver.find_element(By.XPATH, '//div[@class="o0Svhf"]/span/span/span').text.strip() if driver.find_elements(By.XPATH, '//div[@class="o0Svhf"]/span/span/span') else "Not Specified"  # status
            l.append("Functioning" if status in {"Open", "Closed", "Closes soon"} else status)

            l.append(driver.find_element(By.XPATH, '//div[@class="F7nice "]/span/span[@aria-hidden="true"]').text.strip() if driver.find_elements(By.XPATH, '//div[@class="F7nice "]/span/span[@aria-hidden="true"]') else "Not Specified")  # rating

            l.append(driver.find_element(By.XPATH, '//div[@class="RcCsl fVHpi w4vB1d NOE9ve M0S7ae AG25L "]//button[@data-tooltip="Copy phone number"]//div[@class="Io6YTe fontBodyMedium kR99db "]').text.strip() if driver.find_elements(By.XPATH, '//div[@class="RcCsl fVHpi w4vB1d NOE9ve M0S7ae AG25L "]//button[@data-tooltip="Copy phone number"]//div[@class="Io6YTe fontBodyMedium kR99db "]') else "No Specified")  # phone

            # Continue the rest of the code...
            l.append(driver.find_element(By.CSS_SELECTOR, 'div.RcCsl:nth-child(3) > button:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)').text.strip() if driver.find_elements(By.CSS_SELECTOR, 'div.RcCsl:nth-child(3) > button:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)') else "No Specified")  # address

            l.append(ele.get_attribute("href"))  # link

            full_list.append(l)
            print(l)

        with open(f"results_in_{loc}.csv", 'w') as r:
            writer = csv.writer(r)
            writer.writerows(full_list)
            r.close()
            break
    except StaleElementReferenceException:
            print('staled')


et1 = time.time()
et2 = time.time()
print(et1, " ", et2, " ", et1 - st)
