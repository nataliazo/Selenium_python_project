from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from .base_page import BasePage



class ProductPage(BasePage):

    def shoud_be_product_page(self):
        self.should_be_url()
        self.should_be_write_review()
        self.should_be_price()

    def should_be_url(self):
        assert "?promo=newYear" in self.browser.current_url, "?promo=newYear - missing on the URL"

    def should_be_add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.Add_TO_CART), "add to cart button is missing"

    def should_be_write_review(self):
        assert self.is_element_present(*ProductPageLocators.WRITE_REVIEW), "write review CTA is missing"

    def should_be_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_COLOR), "price is missing"

    def return_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.MAIN_BOOK_NAME)
        return book_name.text

    def return_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        return book_price.text

    def should_be_thing_in_basket(self, book_name):
        alert_book_name = self.browser.find_element(*ProductPageLocators.ALERT_BOOK_NAME)
        assert book_name == alert_book_name.text, "book name is {}, but alert book name is {}".format(book_name,
                                                                                                      alert_book_name.text)
        # main_book_name = self.browser.find_element(*ProductPageLocators.MAIN_BOOK_NAME)
        # assert main_book_name.text == alert_book_name.text, "book name is {}, but alert book name is {}".format(main_book_name.text, alert_book_name.text)

    def should_be_same_price(self, book_price):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert basket_price.text == book_price, "basket prise is {}, but book price is {}".format(basket_price.text,
                                                                                                  book_price)
        # book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        # assert basket_price.text == book_price.text, "basket prise is {}, but book price is {}".format(basket_price.text, book_price.text)





    def add_to_cart(self):
        add_to_cart_link = self.browser.find_element(*ProductPageLocators.Add_TO_CART)
        add_to_cart_link.click()

    def go_to_alert(self):
        self.solve_quiz_and_get_code()


