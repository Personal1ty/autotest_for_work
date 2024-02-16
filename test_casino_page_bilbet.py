from .pages.login_page_bilbet import LoginPageBilbet
from .pages.casino_page_bilbet import CasinoPageBilbet
from .pages.deposits_page_bilbet import CasinoDepositsPage
import time
import pytest
from .accesses_config import Accesses



class TestLoginPage():
    @pytest.mark.skip
    def test_guest_can_do_to_login_page(self, browser):
        link = Accesses.predprod_adress
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
    @pytest.mark.skip
    def test_guest_can_do_to_casino_page(self, browser):
        link = Accesses.predprod_adress
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = LoginPageBilbet(browser, link)    
        # открываем страницу
        page.open()
        page.clicked_account_auth_button()    
        page.finall_auth_user()
        casino_page = CasinoPageBilbet(browser, browser.current_url)
        casino_page.deposit_popup_close()
        casino_page.verification_popup_close()
        #casino_page.casino_header_logo_home()   #пока не нужен
        casino_page.header_game_buttons()
        casino_page.header_android_button()
        casino_page.casino_banner_carousel()
        casino_page.game_main_page()
        casino_page.footer_socials_buttons()

class TestCasinoDepositPage():
    def test_deposit_page(self, browser):
        link = Accesses.predprod_adress
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = LoginPageBilbet(browser, link)    
        # открываем страницу
        page.open()
        page.clicked_account_auth_button()    
        page.finall_auth_user()
        deposit_page = CasinoDepositsPage(browser, browser.current_url)
        deposit_page.deposit_popup_close()
        deposit_page.get_token()
        deposit_page.create_manual_transaction_for_kassma()
        deposit_page.open_deposit_popup()
        deposit_page.select_paytm()
        deposit_page.input_amount()
        deposit_page.click_pay_button()
        deposit_page.input_transaction_id()


        