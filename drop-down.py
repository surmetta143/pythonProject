from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver= webdriver.Chrome(executable_path="C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

drop_down= Select(driver.find_element_by_xpath("//*[@id='speed']"))
all_options= drop_down.options
for i in all_options:
    if i.text=="Medium":
        break
    else:
        print(i.text)
else:
    print("finally output is printed")



