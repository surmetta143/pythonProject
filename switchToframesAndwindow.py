from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\chromedriver.exe")
#driver= webdriver.Firefox()
driver.get("https://www.redbus.in/")
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#driver.execute_script("window.scrollTo(0,1000)")
element = driver.find_element_by_xpath("//*[@id='advantage']/div[3]/div[1]")
driver.execute_script("arguments[0].scrollintoView();",element)