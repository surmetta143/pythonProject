
class LoginPage1:
    textbox_username_id = "txtUsername"
    textbox_password_id = "txtPassword"
    button_signin_id = "btnLogin"

    def __init__(self,driver):
        self.driver = driver
    def setusername(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
    def setpassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)
    def loginClick(self):
        self.driver.find_element_by_id(self.button_signin_id).click()