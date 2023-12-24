from .base_page import BasePage
from .locators import LoginPageLocatorsBilbet
import time

class LoginPageBilbet(BasePage):
    #нажимаю на кнопку авторизации
    def clicked_login_button(self):
        start_login_button = self.browser.find_element(*LoginPageLocatorsBilbet.CLICK_LOGIN_BUTTON)
        start_login_button.click()

    #ввожу логин    
    def fill_it_out_login(self):
        login_input = self.browser.find_element(*LoginPageLocatorsBilbet.INPUT_EMAIL)
        login_input.send_keys("")
    
    #ввожу пароль
    def fill_it_out_pass(self): 
        pass_input = self.browser.find_element(*LoginPageLocatorsBilbet.INPUT_PASS)
        pass_input.send_keys("")    
    
    #нажимаю на log in, завершаю авторизацию     
    def clicked_authorization_button(self):
        authorization_button = self.browser.find_element(*LoginPageLocatorsBilbet.CLICK_AUTHORIZATION_BUTTON)
        authorization_button.click()    
        time.sleep(3)