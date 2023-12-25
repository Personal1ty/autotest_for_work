from .locators import RegisterPageLocatorsBilbet
from selenium.webdriver.support.ui import Select
from .base_page import BasePage

import time

class RegisterPageBilbet(BasePage):
    def clicked_register_page(self):
        start_register_button = self.browser.find_element(*RegisterPageLocatorsBilbet.CLICK_REGISTER_BUTTON)
        start_register_button.click()

    def check_select_currency(self):
        #проверка валют общая + каждая валюта, все должны быть по умолчанию включены
        assert self.is_element_present(*RegisterPageLocatorsBilbet.ACCOUNT_CURRENCY_SELECT), "currency OFF"
        assert self.is_element_present(*RegisterPageLocatorsBilbet.ACCOUNT_CURRENCY_INR), "currency INR OFF"
        assert self.is_element_present(*RegisterPageLocatorsBilbet.ACCOUNT_CURRENCY_UZS), "currency UZS OFF"  
        assert self.is_element_present(*RegisterPageLocatorsBilbet.ACCOUNT_CURRENCY_BDT), "currency BDT OFF"

        #тут добавить выбор локали!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        time.sleep(3)
    def check_welcome_bonus(self):
        click_account_currency = self.browser.find_element(*RegisterPageLocatorsBilbet.REG_WELCOME_BONUS)
        click_account_currency.click()
        time.sleep(3)
        assert self.is_element_present(*RegisterPageLocatorsBilbet.REG_WELCOME_BONUS_CASINO), "casino bonus OFF"
        assert self.is_element_present(*RegisterPageLocatorsBilbet.REG_WELCOME_BONUS_SPORT), "sport bonus OFF"
        assert self.is_element_present(*RegisterPageLocatorsBilbet.REG_WELCOME_BONUS_PROMOCODE), "promocode bonus OFF"
