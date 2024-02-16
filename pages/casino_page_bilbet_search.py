from .base_page import BasePage
from .locators import CasinoPageSearchLocatorsBilbet
from .locators import GeneralPageLocators
import time



class CasinoPageBilbetSearch(BasePage):
     def deposit_popup_close(self):
        #deposit_popup = self.is_element_present(*GeneralPageLocators.CLOSE_MOBILE_DEP_POPUP)
        #if deposit_popup == True:
        self.browser.find_element(*GeneralPageLocators.CLOSE_MOBILE_DEP_POPUP).click()
        print("deposit popup close")   

     def game_container_for_popular_success_open(self):
        assert self.is_element_present(*CasinoPageSearchLocatorsBilbet.CHECK_GAME_CONTAINER_FOR_POPULAR), "game container is not open"
        #закрытие попапа с депозитами

     def input_search_game_name(self): 
        return self.browser.find_element(*CasinoPageSearchLocatorsBilbet.INPUT_SEARCH_CASINO_GAME) 

     def casino_header_search(self):
        search_element_click = self.browser.find_element(*CasinoPageSearchLocatorsBilbet.HEADER_SEARCH_CASINO_GAME)
        search_element_click.click()
        self.game_container_for_popular_success_open()

        self.input_search_game_name.send_keys("te")
        assert self.is_element_present(*CasinoPageSearchLocatorsBilbet.USER_CASINO_SEARCH_ERROR), 'error casino search is not'

        self.input_search_game_name.send_keys("Royal Coins 2: Hold and Win")
        
        playng_search_game_mobile = self.is_element_present(*GeneralPageLocators.PLAY_MOBILE_CASINO_GAME)
        if playng_search_game_mobile == True:
            self.browser.find_element(*GeneralPageLocators.PLAY_MOBILE_CASINO_GAME).click()
        #time.sleep(3)
        self.deposit_popup_close()

        #self.game_container_success_open()
        print("casino header search success")
        time.sleep(3)