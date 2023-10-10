from .base_page import BasePage
from .locators import ProductPageLocators


class PageObject(BasePage):
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        link.click()
