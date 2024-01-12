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
        #проверка успешного отображения категории популярных игр
    def game_container_for_popular_success_open(self):
        assert self.is_element_present(*CasinoPageLocatorsBilbet.CHECK_GAME_CONTAINER_FOR_POPULAR), "game container is not open"
        #закрытие попапа с депозитами
    def deposit_popup_close(self):
        deposit_popup = self.is_element_present(*GeneralPageLocators.CLOSE_MOBILE_DEP_POPUP)
        if deposit_popup == True:
            self.browser.find_element(*GeneralPageLocators.CLOSE_MOBILE_DEP_POPUP).click()
        #закрытие и проверка поапа с верификацией    
    def verification_popup(self):        
        #проверяем, есть ли попап с просьбой о верификации, почему то иногда не появляется
        verification_popup = self.is_element_present(*CasinoPageLocatorsBilbet.VERIFICATION_POPUP)
        if verification_popup == True:
            self.browser.find_element(*CasinoPageLocatorsBilbet.VERIFICATION_POPUP).click()
            print("verification popup close")
        else:
            print("verification popup is not")
        #проверка наличия кнопки авиатор в хедере сайта            
    def header_aviator_button(self):
        assert self.is_element_present(*CasinoPageLocatorsBilbet.HEADER_AVIATOR_BUTTON), "aviator button in header is not"
        print("aviator button success")
        #проверка кнопки скачивания приложения в хедере сайта 
    def header_android_button(self):
        assert self.is_element_present(*CasinoPageLocatorsBilbet.HEADER_ANDROID_BUTTON), "download android button is not"
        print("download android button button success")
        #проверка поиска игр через серч    
    def casino_header_search(self):
        search_element_click = self.browser.find_element(*CasinoPageLocatorsBilbet.HEADER_SEARCH_CASINO_GAME)
        search_element_click.click()
        self.game_container_for_popular_success_open()

        input_search = self.browser.find_element(*CasinoPageLocatorsBilbet.INPUT_SEARCH_CASINO_GAME)
        input_search.send_keys("Royal Coins 2: Hold and Win")
        
        playng_search_game_mobile = self.is_element_present(*GeneralPageLocators.PLAY_MOBILE_CASINO_GAME)
        if playng_search_game_mobile == True:
            self.browser.find_element(*GeneralPageLocators.PLAY_MOBILE_CASINO_GAME).click()
        
        self.deposit_popup_close()

        #self.game_container_success_open()
        self.app_header_logo()
        print("casino header search success")  