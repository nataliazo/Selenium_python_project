from selenium.webdriver.common.by import By

#каждый селектор — это пара: как искать и что искать.
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    SHOPPING_CART = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_BASCKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    ITEMS_IN_BASKET_MESSAGE = (By.CSS_SELECTOR, ".hidden-xs")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PW = (By.CSS_SELECTOR, "id_registration-email")
    REGISTER_PW2 = (By.CSS_SELECTOR,"id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "id_registration-redirect_url")


class ProductPageLocators():
    Add_TO_CART = (By.CSS_SELECTOR,".btn-add-to-basket")
    WRITE_REVIEW = (By.CSS_SELECTOR,"#write_review")
    PRICE_COLOR = (By.CSS_SELECTOR,".price_color")
    MAIN_BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ALERT_BOOK_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,".alert-success")


