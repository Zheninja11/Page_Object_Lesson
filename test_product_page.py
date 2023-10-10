from .pages.main_page import MainPage
from .pages.product_page import PageObject
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = PageObject(browser, link, timeout=5)
    page.open()
    page.add_to_basket()
    time.sleep(2)
    page.solve_quiz_and_get_code()
    
    