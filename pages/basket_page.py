from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def basket_should_have_empty_message(self):
        assert self.is_element_present (*BasketPageLocators.EMPTY_BASCKET_MESSAGE), "The basket is not empty as it should be"

    def basket_hasnt_items(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET_MESSAGE), "Some items are in the basket, but they shouldnt"

