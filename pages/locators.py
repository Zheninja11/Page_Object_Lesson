from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    REGISTER_FORM = (By.XPATH, "//form[@id='register_form']")
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")