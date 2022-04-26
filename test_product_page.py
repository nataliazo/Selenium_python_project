import pytest
import time

from .pages.product_page import ProductPage

#@pytest.mark.parametrize("offer_number", ["0", "1" ,"2", "3", "4","5","6","7","8","9"])
#@pytest.mark.parametrize('link', ["okay_link", pytest.param("bugged_link", marks=pytest.mark.xfail), "okay_link"])

#def test_guest_can_add_product_to_basket(browser, offer_number, link):
    #link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer{offer_number}"
    #page = ProductPage(browser, link)
    #page.open()
    #page.shoud_be_product_page()
    #page.add_to_cart()
    #page.go_to_alert()
    #book_name = page.return_book_name()
    #page.should_be_same_price(book_price)
    #page.should_be_thing_in_basket(book_name)

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.shoud_be_product_page()
    page.add_to_cart()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.shoud_be_product_page()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.shoud_be_product_page()
    page.add_to_cart()
    time.sleep(1)
    page.allert_message_should_dessapere()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()











if __name__ == "__main__":
    pytest.main()

