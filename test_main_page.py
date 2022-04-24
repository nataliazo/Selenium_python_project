from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    #page object initialisation, pass the browser an url to the constructor
    page = MainPage(browser, link)
    page.open() #open the page
    page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина