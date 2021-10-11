from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver= webdriver.Chrome(executable_path="C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
elemet5=driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")
drag_drop_source=driver.find_element_by_xpath("//*[@id='draggable']/p")
drag_drop_target=driver.find_element_by_xpath("//*[@id='droppable']")
resize= driver.find_element_by_xpath("//*[@id='slider']/span")
resize_page=driver.find_element_by_xpath("//*[@id='resizable']/div[3]")
actions= ActionChains(driver)
actions.double_click()
actions.drag_and_drop(drag_drop_source,drag_drop_target).perform()
actions.drag_and_drop_by_offset(resize,100,0).perform()
actions.drag_and_drop_by_offset(resize_page,100,100).perform()


