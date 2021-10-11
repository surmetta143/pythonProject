import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from XLutilities.cutsomlogs import Test_Base_log
@pytest.fixture()
def setup():

    chrome_options= webdriver.ChromeOptions()
    prefs={"profile.default_content_setting_values_notifications":2}
    chrome_options.add_experimental_option("prefs",prefs)
    chrome_options.add_argument("--disable-notifications")

    driver=webdriver.Chrome(chrome_options=chrome_options)
    return driver

def test_loginFb(setup):
    driver = setup
    driver.get("https://www.facebook.com/login/")
    print(driver.title)
    log=Test_Base_log.log_name()
    driver.close()
    log.info("test is passed")


def test_loginFb1(setup):
    driver = setup


    driver.get("https://www.facebook.com/login/")
    driver.find_element_by_xpath("//*[@id='email']").send_keys("mskmouni@gmail.com")
    driver.find_element_by_xpath("//*[@id='pass']").send_keys("cdsdcdsd")
    print(driver.title)
    Test_Base_log.log_name().info("test is passed")
    driver.close()


def test_loginFb2(setup):
    driver = setup
    driver.get("https://www.facebook.com/login/")
    driver.find_element_by_xpath("//*[@id='email']").send_keys("mskmouni@gmail.com")
    driver.find_element_by_xpath("//*[@id='pass']").send_keys("cdsdcdsd")
    driver.find_element_by_xpath("//*[@id='loginbutton']").click()
    print(driver.title)
    Test_Base_log.log_name().info("test is passed succssfully")
    driver.close()




