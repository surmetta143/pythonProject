from selenium import webdriver
import pytest
from pageobjetcs.Loginpage import LoginPage1
from XLutilities.readProporties import Readconfig

class Test_001_Login:
    baseurl = Readconfig.getApplicationurl()
    username = Readconfig.getApplicationUsername()
    password= Readconfig.getApplicationPassword()

    def test_homepageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title=self.driver.title
        if act_title=="OrangeHRM":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screeshots\\"+"test_homepageTitle.png")
            self.driver.close()
            assert False
    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp=LoginPage1(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.loginClick()
        act_title = self.driver.title
        self.driver.close()
        if act_title=="OrangeHRM":
            assert True
        else:
            assert False
