from .pages.login_page_bilbet import LoginPageBilbet
from .pages.casino_page_bilbet import CasinoPageBilbet
import time
import pytest



class TestLoginPage():
    @pytest.mark.skip
    def test_guest_can_do_to_login_page(self, browser):
        link = "https://preprodappbets.dimatech.org/"
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = LoginPageBilbet(browser, link)    
        # открываем страницу
        page.open()                      
        # выполняем метод страницы — переходим на страницу логина
        page.clicked_account_auth_button()
        page.check_error_email_and_pass_auth_popup()
        page.chek_error_phone_number_auth_popup()         
        page.finall_auth_user()

class TestMainCasinoPage():
    #@pytest.mark.skip
    def test_guest_can_do_to_casino_page(self, browser):
        link = "https://preprodappbets.dimatech.org/"
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = LoginPageBilbet(browser, link)    
        # открываем страницу
        page.open()
        page.clicked_account_auth_button()    
        page.finall_auth_user()
        casino_page = CasinoPageBilbet(browser, browser.current_url)
        casino_page.verification_popup()