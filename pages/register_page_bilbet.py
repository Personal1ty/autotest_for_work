from .locators import RegisterPageLocatorsBilbet
from .base_page import BasePage
import time

class RegisterPageBilbet(BasePage):
    def clicked_register_popup(self):
        start_register_button = self.browser.find_element(*RegisterPageLocatorsBilbet.CLICK_REGISTER_BUTTON)
        start_register_button.click()
        print("click registration button")

    #проверка валют общая + каждая валюта, все должны быть по умолчанию включены
    def check_select_currency_register_popup(self):
        assert self.is_element_present(*RegisterPageLocatorsBilbet.ACCOUNT_CURRENCY_SELECT), "currency OFF"
        choose_account_currency = self.browser.find_element(*RegisterPageLocatorsBilbet.ACCOUNT_CURRENCY_SELECT)
        choose_account_currency.click()
        assert self.is_element_present(*RegisterPageLocatorsBilbet.ACCOUNT_CURRENCY_INR), "currency INR OFF"
        assert self.is_element_present(*RegisterPageLocatorsBilbet.ACCOUNT_CURRENCY_UZS), "currency UZS OFF"  
        assert self.is_element_present(*RegisterPageLocatorsBilbet.ACCOUNT_CURRENCY_BDT), "currency BDT OFF"
        print("check currency register popup")
    
    #Проверка велком бонусов
    def check_welcome_bonus_inr_register_popup(self):
        choose_account_currency = self.browser.find_element(*RegisterPageLocatorsBilbet.ACCOUNT_CURRENCY_INR)
        choose_account_currency.click()
        click_welcome_bonus = self.browser.find_element(*RegisterPageLocatorsBilbet.REG_WELCOME_BONUS)
        click_welcome_bonus.click()        
        assert self.is_element_present(*RegisterPageLocatorsBilbet.REG_WELCOME_BONUS_CASINO), "casino bonus OFF"
        assert self.is_element_present(*RegisterPageLocatorsBilbet.REG_WELCOME_BONUS_SPORT), "sport bonus OFF"
        assert self.is_element_present(*RegisterPageLocatorsBilbet.REG_WELCOME_BONUS_PROMOCODE), "promocode bonus OFF"
        click_casino_bonus = self.browser.find_element(*RegisterPageLocatorsBilbet.REG_WELCOME_BONUS_CLICK_CASINO)
        click_casino_bonus.click()
        time.sleep(3)
        print("check bonus register popup")
    
    #проверка ошибки логина и пароля, логин без собаки, пароль короткий
    def check_correct_email_and_pass_register_popup(self):
        input_register_login = self.browser.find_element(*RegisterPageLocatorsBilbet.INPUT_LOGIN)
        input_register_login.send_keys("test")
        input_register_pass = self.browser.find_element(*RegisterPageLocatorsBilbet.INPUT_PASS)
        input_register_pass.send_keys("pass")
        click_register_button = self.browser.find_element(*RegisterPageLocatorsBilbet.CLICK_CREATE_ACCOUNT)
        click_register_button.click()
        assert self.is_element_present(*RegisterPageLocatorsBilbet.REGISTER_EMAIL_ERROR), "No error if input incorrect email"
        assert self.is_element_present(*RegisterPageLocatorsBilbet.REGISTER_PASS_ERROR), "No error if input incorrect pass"
        print("check error register popup")
    
    #региструем пользователя
    def input_registration_credentials_register_popup(self):
        self.browser.find_element(*RegisterPageLocatorsBilbet.INPUT_LOGIN).clear()
        input_register_login = self.browser.find_element(*RegisterPageLocatorsBilbet.INPUT_LOGIN)
        user_credentials = str(time.time())
        input_register_login.send_keys("test" + user_credentials + "@gmail.com")
        self.browser.find_element(*RegisterPageLocatorsBilbet.INPUT_PASS).clear()
        input_register_pass = self.browser.find_element(*RegisterPageLocatorsBilbet.INPUT_PASS)
        input_register_pass.send_keys(user_credentials)
        click_register_button = self.browser.find_element(*RegisterPageLocatorsBilbet.CLICK_CREATE_ACCOUNT)
        click_register_button.click()
        assert self.is_element_present(*RegisterPageLocatorsBilbet.REGISTRATION_POPUP), "registeration not finish "
        print("registration user register popup")    
