from selenium.common.exceptions import NoSuchElementException
class BasePage():
    #объявляем конструктор __init__ В него в качестве параметров мы передаем экземпляр драйвера и url адрес.
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # реализуем метод is_element_present, в котором будем перехватывать исключение. В него будем передавать два аргумента:
    # как искать (css, id, xpath и тд) и собственно что искать (строку-селектор);
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    #добавим еще один метод open. Он должен открывать нужную страницу в браузере, используя метод get().
    def open (self):
        self.browser.get(self.url)
