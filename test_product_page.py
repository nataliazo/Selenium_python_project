from .pages.product_page import ProductPage
from .pages.main_page import MainPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.shoud_be_product_page()
    page.add_to_cart()
    page.go_to_alert()
