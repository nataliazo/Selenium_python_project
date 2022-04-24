class BasePage():
    #объявляем конструктор __init__ В него в качестве параметров мы передаем экземпляр драйвера и url адрес.
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    #добавим еще один метод open. Он должен открывать нужную страницу в браузере, используя метод get().
    def open (self):
        self.browser.get(self.url)
