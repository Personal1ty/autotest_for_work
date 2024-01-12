from .base_page import BasePage
from .locators import CasinoPageLocatorsBilbet
from .locators import GeneralPageLocators
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='app.log')


class CasinoPageBilbet(BasePage):
        #возврат на главную страницу сайта путем нажатия на иконку в хедере
    def app_header_logo(self):
        app_header_logo = self.browser.find_element(*CasinoPageLocatorsBilbet.APP_HEADER_LOGO)
        return app_header_logo.click()
        #проверка успешного открытия окна игры
    def game_container_success_open(self):
        assert self.is_element_present(*CasinoPageLocatorsBilbet.CHECK_GAME_CONTAINER), "game not open"
    def deposit_popup(self):
        deposit_popup = self.is_element_present(*GeneralPageLocators.CLOSE_MOBILE_DEP_POPUP)
        if deposit_popup == True:
            self.browser.find_element(*GeneralPageLocators.CLOSE_MOBILE_DEP_POPUP).click()
    def verification_popup(self):        
        #проверяем, есть ли попап с просьбой о верификации, почему то иногда не появляется
        verification_popup = self.is_element_present(*CasinoPageLocatorsBilbet.VERIFICATION_POPUP)
        if verification_popup == True:
            self.browser.find_element(*CasinoPageLocatorsBilbet.VERIFICATION_POPUP).click()
    def header_aviator_button(self):
        assert self.is_element_present(*CasinoPageLocatorsBilbet.HEADER_AVIATOR_BUTTON), "aviator button in header is not"
    def header_android_button(self):
        assert self.is_element_present(*CasinoPageLocatorsBilbet.HEADER_ANDROID_BUTTON), "download android button is not"    
    def casino_header_search(self):
        search_element_click = self.browser.find_element(*CasinoPageLocatorsBilbet.HEADER_SEARCH_CASINO_GAME)
        search_element_click.click()
        time.sleep(5)
        input_search = self.browser.find_element(*CasinoPageLocatorsBilbet.INPUT_SEARCH_CASINO_GAME)
        input_search.send_keys("Royal Coins 2: Hold and Win")
        time.sleep(5)
        playng_search_game_mobile = self.is_element_present(*GeneralPageLocators.PLAY_MOBILE_CASINO_GAME)
        #if playng_search_game_mobile == True:
        #    self.browser.find_element(*GeneralPageLocators.PLAY_MOBILE_CASINO_GAME).click()
        self.browser.find_element(*GeneralPageLocators.PLAY_MOBILE_CASINO_GAME).click()
        self.deposit_popup()
        #playng_search_game = self.browser.find_element(*CasinoPageLocatorsBilbet.PLAYNG_SEARCH_GAME)
        #playng_search_game.click()
        #self.game_container_success_open()
        self.app_header_logo()
