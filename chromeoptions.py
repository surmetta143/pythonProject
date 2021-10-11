from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notificatons":2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--disable-notifications")
driver=webdriver.Chrome(executable_path="C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\chromedriver.exe",chrome_options=chrome_options)
driver.get("https://www.facebook.com/login/")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='email']").send_keys("mskmouni@gmail.com")
driver.find_element_by_xpath("//*[@id='pass']").send_keys("cdsdcdsd")
driver.find_element_by_xpath("//*[@id='loginbutton']").click()
print(driver.title)
