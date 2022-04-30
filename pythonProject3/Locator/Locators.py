from selenium.webdriver.common.by import By

#HomePage

cartPressLocator = (By.ID, "nav-cart-count")

#ShoppingCartPage

item1 = (By.XPATH, "(//input[@value = 'Delete'])[1]")
allItems = (By.XPATH, "//div[@data-itemcategory='normal']")

#LoginPage

theUserName = (By.NAME, "email")
continueButton = (By.CLASS_NAME, "a-button-input")
thePassword = (By.ID, "ap_password")
checkbox = (By.NAME, "rememberMe")
signInAmazon = (By.CLASS_NAME, "a-button-input")