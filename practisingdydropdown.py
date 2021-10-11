import time

from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.F
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
time.sleep(10)
webdriver(driver,10).until(EC.presence_of_element_located(driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div/div[2]/div[1]/div[1]/label").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/input").send_keys("del")
elements=driver.find_elements_by_xpath("//li[@class='react-autosuggest__suggestion']")
print(len(elements))
for city in elements:
    if city.text=="New Delhi, India":
         city.click()
