from .base_page import BasePage
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "url isn't correct"
        assert True

    def should_be_login_form(self):
        self.is_element_present(*MainPageLocators.LOGIN_FORM), "Login form input is not presented"
        assert True

    def should_be_register_form(self):
        self.is_element_present(*MainPageLocators.REGISTER_FORM), "Registration form input is not presented"
        assert True
