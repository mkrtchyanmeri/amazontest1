from Locator.Locators import *

class AmazonHomePageclass():
    def __init__(self, driver):
        self.driver = driver

    def press_cart(self):
        AmazonCart = self.driver.find_element(*cartPressLocator)
        AmazonCart.click()