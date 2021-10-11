from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")
print(driver.get_cookies())
try:
    cooki= {'suresh':'you'}
    driver.add_cookie(cooki)
    print(driver.get_cookies())
    driver.delete_cookie(cooki)
    print(driver.get_cookies())
except:
     driver.close()