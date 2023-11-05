from selenium.webdriver.common.by import By


class LoginPageLocators():
    REGISTER_FORM = (By.XPATH, "//form[@id='register_form']")
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTER_INPUT_EMAIL = (By.XPATH, "//input[@id='id_registration-email']")
    REGISTER_INPUT_PASSWORD = (By.XPATH, "//input[@id='id_registration-password1']")
    REGISTER_INPUT_PASSWORD_CONFIRM = (By.XPATH, "//input[@id='id_registration-password2']")
    REGISTER_BUTTON_REGISTER = (By.XPATH, "//button[@name='registration_submit']")
    
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    PRODUCT_PRICE_PAGE = (By.CSS_SELECTOR, ".product_main > .price_color")
    PRODUCT_PRICE_BASKET = (By.CSS_SELECTOR, ".basket-mini")
    PRODUCT_NAME_PAGE = (By.CSS_SELECTOR, " div > h1")
    PRODUCT_NAME_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//a[@class='btn btn-default']")
    BUTTON_GO_TO_CHECKOUT = (By.XPATH, "//a[@class='btn.btn-lg.btn-primary.btn-block']")
    TXT_YOUR_BASKET_IS_EMPTY = (By.XPATH, "//div[@id='content_inner']/p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")