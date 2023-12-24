#from .pages.main_page import MainPage
from .pages.login_page_bilbet import LoginPageBilbet


def test_guest_can_do_to_login_page(browser):
    link = "https://preprodappbets.dimatech.org/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = LoginPageBilbet(browser, link)    
    # открываем страницу
    page.open()                      
    # выполняем метод страницы — переходим на страницу логина
    page.clicked_login_button()         
    page.fill_it_out_login()
    page.fill_it_out_pass()
    page.clicked_authorization_button()
   