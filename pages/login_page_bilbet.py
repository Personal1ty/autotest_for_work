from .base_page import BasePage
from .locators import LoginPageLocatorsBilbet
import time

class LoginPageBilbet(BasePage):

    def clicked_auth_button(self):
        start_login_button = self.browser.find_element(*LoginPageLocatorsBilbet.CLICK_LOGIN_BUTTON)
        start_login_button.click()
        print("click login button")
    
    def check_error_email_and_pass_auth_popup(self): 
        login_input = self.browser.find_element(*LoginPageLocatorsBilbet.INPUT_EMAIL)
        login_input.send_keys("test")
        pass_input = self.browser.find_element(*LoginPageLocatorsBilbet.INPUT_PASS)
        pass_input.send_keys("test")
        authorization_button = self.browser.find_element(*LoginPageLocatorsBilbet.CLICK_AUTHORIZATION_BUTTON)
        authorization_button.click()
        assert self.is_element_present(*LoginPageLocatorsBilbet.LOGIN_ERROR), "LOGIN ERROR IS NOT"
        assert self.is_element_present(*LoginPageLocatorsBilbet.PASS_ERROR), "PASS ERROR IS NOT"
        assert self.is_element_present(*LoginPageLocatorsBilbet.FORGOT_PASSWORD), "FOGOT PASSWORD IS NOT"
        print("check error auth popup")
          
    def chek_error_phone_number_auth_popup(self):
        click_phone = self.browser.find_element(*LoginPageLocatorsBilbet.CLICK_PHONE)
        click_phone.click()
        input_phone = self.browser.find_element(*LoginPageLocatorsBilbet.INPUT_PHONE)
        input_phone.clear()
        input_phone.send_keys("78478")
        input_pass = self.browser.find_element(*LoginPageLocatorsBilbet.INPUT_PASS)
        input_pass.send_keys("test")
        authorization_button = self.browser.find_element(*LoginPageLocatorsBilbet.CLICK_AUTHORIZATION_BUTTON)
        authorization_button.click()
        assert self.is_element_present(*LoginPageLocatorsBilbet.PHONE_ERROR), "PHONE ERROR IS NOT"
        assert self.is_element_present(*LoginPageLocatorsBilbet.PASS_ERROR), "PASS ERROR IS NOT"
        print("check error auth for phone popup")        
    #ввожу логин    
    def finall_auth_user(self):
        login_input = self.browser.find_element(*LoginPageLocatorsBilbet.INPUT_EMAIL)
        login_input.send_keys("test") 
        pass_input = self.browser.find_element(*LoginPageLocatorsBilbet.INPUT_PASS)
        pass_input.send_keys("")    
        authorization_button = self.browser.find_element(*LoginPageLocatorsBilbet.CLICK_AUTHORIZATION_BUTTON)
        authorization_button.click()    
        time.sleep(3)
        print("user login success") 