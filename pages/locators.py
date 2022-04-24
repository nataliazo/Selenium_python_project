from selenium.webdriver.common.by import By

#каждый селектор — это пара: как искать и что искать.
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    Add_TO_CART = (By.CSS_SELECTOR,".btn-add-to-basket")
    WRITE_REVIEW = (By.CSS_SELECTOR,"#write_review")
    PRICE_COLOR = (By.CSS_SELECTOR,".price_color")
    MAIN_BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ALERT_BOOK_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
