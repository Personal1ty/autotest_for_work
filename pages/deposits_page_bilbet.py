from .base_page import BasePage
from .locators import CasinoPageLocatorsBilbet
from .locators import GeneralPageLocators
from .locators import CasinoPageDepositLocatorsBilbet
import time
from selenium.webdriver.common.by import By
import time




class CasinoDepositsPage(BasePage):
    
    def deposit_popup_close(self):  #временный метод, после связи удалить
        time.sleep(3)
        deposit_popup = self.is_element_present(*GeneralPageLocators.CLOSE_MOBILE_DEP_POPUP)
        if deposit_popup == True:
           print("deposit popup close")
           return self.browser.find_element(*GeneralPageLocators.CLOSE_MOBILE_DEP_POPUP).click()
        else:
            print("there is money in the account") 
        

            

    def verification_popup_close(self):            
        #проверяем, есть ли попап с просьбой о верификации, почему то иногда не появляется
        verification_popup = self.is_element_present(*CasinoPageLocatorsBilbet.VERIFICATION_POPUP)
        if verification_popup == True:
            self.browser.find_element(*CasinoPageLocatorsBilbet.VERIFICATION_POPUP).click()
            print("verification popup close")
        else:
            print("verification popup is not")     

        
    def open_deposit_popup(self):
        open_deposit_popup = self.browser.find_element(*CasinoPageLocatorsBilbet.INPUT_DEP)
        open_deposit_popup.click()
        print("<<<1>>>")

    def check_deposit_categories_carousel(self):
        check_deposit_categories_carousel = self.browser.find_element(By.CSS_SELECTOR, '[class="deposit-categories-carousel__category swiper-slide deposit-categories-carousel__category--active"]')  

    def select_paytm(self):
        open_deposit_popup = self.browser.find_element(*CasinoPageDepositLocatorsBilbet.SELECT_PAYTM)
        open_deposit_popup.click()
        print("<<<2>>>")

    def input_amount(self):
        time.sleep(2)
        input_amount = self.browser.find_element(*CasinoPageDepositLocatorsBilbet.SELECT_DEPOSIT_AMOUNT)       
        input_amount.click()
        print("<<<3>>>")

    def click_pay_button(self):
        click_pay_button = self.browser.find_element(*CasinoPageDepositLocatorsBilbet.PAY_BUTTON)       
        click_pay_button.click()
        print("<<<4>>>")

    def input_transaction_id(self, transaction_id):
        input_transaction_id = self.browser.find_element(*CasinoPageDepositLocatorsBilbet.INPUT_TRANSACTION_ID)
        input_transaction_id.send_keys(transaction_id)
        time.sleep(3)       
     
