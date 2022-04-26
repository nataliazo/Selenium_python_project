from selenium.webdriver.common.by import By
from .base_page import BasePage # импорт базового класса BasePage
from .locators import MainPageLocators

#Go to login page:
def go_to_login_page(self):
    link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    link.click()
    # return LoginPage(browser=self.browser, url=self.browser.current_url)


class MainPage(BasePage):

    #В классе MainPage у нас не осталось никаких методов, поэтому добавим туда заглушку:
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)


