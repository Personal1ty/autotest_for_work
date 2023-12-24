from .locators import RegisterPageLocatorsBilbet
from selenium.webdriver.support.ui import Select
from .base_page import BasePage

import time

class RegisterPageBilbet(BasePage):
    def clicked_register_page(self):
        start_register_button = self.browser.find_element(*RegisterPageLocatorsBilbet.CLICK_REGISTER_BUTTON)
        start_register_button.click()

    def check_select_currency(self):
        assert self.is_element_present(*RegisterPageLocatorsBilbet.ACCOUNT_CURRENCY_ALL), "currency ON"
        #select_account_currency = self.browser.find_element(*RegisterPageLocatorsBilbet.ACCOUNT_CURRENCY_ALL)
        #select_account_currency.click()
        select_currency =  Select(self.browser.find_element(*RegisterPageLocatorsBilbet.ACCOUNT_CURRENCY_ALL))
        assert select_currency.select_by_index("1"), "1"
        assert select_currency.select_by_index("2"), "2"
        assert select_currency.select_by_index("3"), "3"
    #def select_account_currency(self):
    #    return