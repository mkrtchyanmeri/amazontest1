from Locator.Locators import *

class AmazonLoginTC():
    def __init__(self, driver):
        self.driver = driver

    def fill_username_fill(self, text):
        username = self.driver.find_element(*theUserName)
        username.clear()
        username.send_keys(text)

    def press_continue_button(self):
        continuebtn = self.driver.find_element(*continueButton)
        continuebtn.click()

    def fill_password_fill(self, passwordText):
        password = self.driver.find_element(*thePassword)
        password.clear()
        password.send_keys(passwordText)

    def check_checkbox(self):
        check = self.driver.find_element(*checkbox)
        check.click()

    def press_signin_button(self):
        signIn = self.driver.find_element(*signInAmazon)
        signIn.click()