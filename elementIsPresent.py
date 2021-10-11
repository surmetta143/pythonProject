from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome(executable_path="C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\chromedriver.exe")
driver.get("https://login.salesforce.com/")
check_box= driver.find_element_by_xpath("//*[@id='rememberUn']").click()
print(check_box)
print(driver.find_element_by_xpath("//*[@id='rememberUn']").is_selected())
print(driver.find_element_by_xpath("//*[@id='rememberUn']").is_enabled())
print(driver.find_element_by_xpath("//*[@id='rememberUn']").is_enabled())

