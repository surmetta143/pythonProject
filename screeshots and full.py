from selenium import webdriver
from PIL import Image
driver = webdriver.Chrome(executable_path="C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.save_screenshot("amazon.png")
screenshot= Image.open("amazon.png")
screenshot.show()