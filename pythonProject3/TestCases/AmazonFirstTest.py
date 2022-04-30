import time
import unittest
from selenium import  webdriver
from Pages.AmazonLogin import AmazonLoginTC
from Pages.AmazonHomePage import AmazonHomePageclass
from Pages.AmazonShoppingCartPage import cart_page

class AmazonLoginPageTC(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.loginpage = AmazonLoginTC(self.driver)
        self.homepage = AmazonHomePageclass(self.driver)
        self.cart = cart_page(self.driver)

    def test_LoginTest(self):
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
        self.loginpage.fill_username_fill("merimkrtchyan19981@gmail.com")
        time.sleep(3)
        self.loginpage.press_continue_button()
        self.loginpage.fill_password_fill("MyAmazon_Pasword.12")
        self.loginpage.check_checkbox()
        time.sleep(3)
        self.loginpage.press_signin_button()
        self.homepage.press_cart()
        self.cart.delete_shopping_cart_first_item()
        time.sleep(1)
        #self.cart.delete_all_items_in_cart()
        #time.sleep(3)

    def tearDown(self):
        time.sleep(5)
        self.driver.close()