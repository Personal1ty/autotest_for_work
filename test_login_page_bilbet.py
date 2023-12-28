#from .pages.main_page import MainPage
from .pages.login_page_bilbet import LoginPageBilbet


def test_guest_can_do_to_login_page(browser):
    link = "https://preprodappbets.dimatech.org/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = LoginPageBilbet(browser, link)    
    # открываем страницу
    page.open()                      
    # выполняем метод страницы — переходим на страницу логина
    page.clicked_auth_button()
    page.check_error_email_and_pass_auth_popup()
    page.chek_error_phone_number_auth_popup()         
    page.finall_auth_user()
   