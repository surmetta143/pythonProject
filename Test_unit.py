import unittest
from selenium import webdriver
import xlutils
from xlutilis import ReadData
from selenium.webdriver.common.keys import Keys
class Test_001(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path="C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\chromedriver.exe")
    @classmethod
    def tearDown(self):
        self.driver.close()

    def test_login_facebook(self):
        self.driver.get("https://www.facebook.com/login/")
        self.driver.find_element_by_xpath("//*[@id='email']").send_keys("mskmouni@gmail.com")
        self.driver.find_element_by_xpath("//*[@id='pass']").send_keys("cdsdcdsd")
        self.driver.find_element_by_xpath("//*[@id='loginbutton']").click()
        title_fb=self.driver.title
        self.assertEqual("test_login_facebook",title_fb,"title of the page is unmatched")
    @unittest.skip("this is the test not ready yet")
    def test_redbus(self):
        self.driver.get("https://www.redbus.in/")
        print(self.driver.title)
    @unittest.SkipTest
    def test_opencart(self):
        self.driver.get("https://www.opencart.com/")
        return self.driver.title

if "__name__" == "__main__":
    unittest.main
