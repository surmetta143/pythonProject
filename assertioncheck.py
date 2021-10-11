from selenium import webdriver

driver= webdriver.Chrome(executable_path="C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\chromedriver.exe")
driver.get("https://www.facebook.com/login/")
print(driver.title)
try:
   assert driver.title=="Log in to Facebook", "page title is not matched"
finally:
    print("you successfully completed the test")
    driver.close()