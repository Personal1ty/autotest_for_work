from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_item_in_backet(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_BACKET)
        login_link.click()
        #alert = self.browser.switch_to.alert
        #alert.accept()
        self.solve_quiz_and_get_code()
       
        
   