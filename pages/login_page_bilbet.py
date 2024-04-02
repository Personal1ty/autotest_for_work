from .base_page import BasePage
from .locators import LoginPageLocatorsBilbet
from .locators import GeneralPageLocators


class LoginPageBilbet(BasePage):

    def vpn_message_close(self):
        vpn_message_close = self.is_element_present(*GeneralPageLocators.VPN_MESSAGE)
        if vpn_message_close == True:
            print("VPN messge close")
            return self.browser.find_element(*GeneralPageLocators.VPN_MESSAGE).click()
        else:
            print("VPN message is not")

    def clicked_input_password_button(self):
        return self.browser.find_element(*LoginPageLocatorsBilbet.INPUT_PASS)

    def authorization_button(self):
        authorization_button = self.browser.find_element(*LoginPageLocatorsBilbet.CLICK_AUTHORIZATION_BUTTON)
        authorization_button.click()

    def input_email(self):
        return self.browser.find_element(*LoginPageLocatorsBilbet.INPUT_EMAIL)
        
    def check_password_error(self):
        assert self.is_element_present(*LoginPageLocatorsBilbet.PASS_ERROR), "PASS ERROR IS NOT"
        
    def clicked_account_auth_button(self):
        start_login_button = self.browser.find_element(*LoginPageLocatorsBilbet.CLICK_LOGIN_BUTTON)
        start_login_button.click()
        print("click login button")
    
    def check_error_email_and_pass_auth_popup(self): 
        self.input_email().send_keys("test")        
        self.clicked_input_password_button().send_keys("test")
        self.authorization_button()
        self.check_password_error()        
        assert self.is_element_present(*LoginPageLocatorsBilbet.LOGIN_ERROR), "LOGIN ERROR IS NOT"
        assert self.is_element_present(*LoginPageLocatorsBilbet.FORGOT_PASSWORD), "FOGOT PASSWORD IS NOT"
        print("check error auth popup")
        #подумать как добавить проверку Sign Up
          
    def chek_error_phone_number_auth_popup(self):
        click_phone = self.browser.find_element(*LoginPageLocatorsBilbet.CLICK_PHONE)
        click_phone.click()
        input_phone = self.browser.find_element(*LoginPageLocatorsBilbet.INPUT_PHONE)
        input_phone.clear()
        input_phone.send_keys("78478")
        self.clicked_input_password_button().send_keys("test")
        self.authorization_button()
        assert self.is_element_present(*LoginPageLocatorsBilbet.PHONE_ERROR), "PHONE ERROR IS NOT"
        self.check_password_error()
        click_email = self.browser.find_element(*LoginPageLocatorsBilbet.CLICK_EMAIL)
        click_email.click()
        print("check error auth for phone popup")        
    #ввожу логин    
    def finall_auth_user(self):
        config = BasePage.load_config()
        self.input_email().send_keys(config['username_and_pass_for_bilbet'])
        self.clicked_input_password_button().send_keys(config['username_and_pass_for_bilbet'])
        self.authorization_button()
        print("user login success") 