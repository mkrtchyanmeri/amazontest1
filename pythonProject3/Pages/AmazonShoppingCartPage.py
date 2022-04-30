from Locator.Locators import *

class cart_page():
    def __init__(self, driver):
        self.driver = driver

    def delete_shopping_cart_first_item(self):
        firstItem = self.driver.find_element(*item1)
        firstItem.click()

    """def delete_all_items_in_cart(self):
        items = self.driver.find_element(*allItems)
        while items:
            items.click()"""