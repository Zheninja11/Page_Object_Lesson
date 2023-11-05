from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasePageLocators

class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)