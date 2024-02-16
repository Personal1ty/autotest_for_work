from .base_page import BasePage
from .locators import CasinoPageLocatorsBilbet
from .locators import GeneralPageLocators
import time
import logging
from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='app.log')


class CasinoPageBilbet(BasePage):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
        self.find_element = self.browser.find_element
        #возврат на главную страницу сайта путем нажатия на иконку в хедере

    def casino_header_logo_home(self):
        app_header_logo = self.browser.find_element(*CasinoPageLocatorsBilbet.CASINO_HEADER_HOME_LOGO)
        return app_header_logo.click()
        #проверка успешного отображения категории популярных игр
    def inside_the_game_button_home(self):
        return self.find_element(*GeneralPageLocators.INSIDE_THE_GAME_BUTTON_HOME).click()
    


    # def game_container_for_popular_success_open(self):
    #     assert self.is_element_present(*CasinoPageLocatorsBilbet.CHECK_GAME_CONTAINER_FOR_POPULAR), "game container is not open"
    #     #закрытие попапа с депозитами
    # def deposit_popup_close(self):
    #     #deposit_popup = self.is_element_present(*GeneralPageLocators.CLOSE_MOBILE_DEP_POPUP)
    #     #if deposit_popup == True:
    #     self.browser.find_element(*GeneralPageLocators.CLOSE_MOBILE_DEP_POPUP).click()
    #     print("deposit popup close")    
    #     #закрытие и проверка поапа с верификацией 
    # def input_search_game_name(self): 
    #     return self.browser.find_element(*CasinoPageLocatorsBilbet.INPUT_SEARCH_CASINO_GAME)    

    def deposit_popup_close(self):
        time.sleep(5)
        deposit_popup = self.is_element_present(*GeneralPageLocators.CLOSE_MOBILE_DEP_POPUP)
        if deposit_popup == True:
           return self.find_element(*GeneralPageLocators.CLOSE_MOBILE_DEP_POPUP).click()
        else:
            print("there is money in the account") 
        print("deposit popup close")   

    def verification_popup_close(self):            
        #проверяем, есть ли попап с просьбой о верификации, почему то иногда не появляется
        verification_popup = self.is_element_present(*CasinoPageLocatorsBilbet.VERIFICATION_POPUP)
        if verification_popup == True:
            self.browser.find_element(*CasinoPageLocatorsBilbet.VERIFICATION_POPUP).click()
            print("verification popup close")
        else:
            print("verification popup is not")

        #проверка наличия кнопки авиатор в хедере сайта               
    def header_game_buttons(self):
        assert self.is_element_present(*CasinoPageLocatorsBilbet.HEADER_GAME_BUTTON), "aviator button in header is not"
        self.find_element(*CasinoPageLocatorsBilbet.HEADER_GAME_BUTTON).click()
        time.sleep(5)
        self.deposit_popup_close()
        time.sleep(5)
        assert self.is_element_present(*CasinoPageLocatorsBilbet.HEADER_GAME_BUTTON_2), "jet x button in header is not"
        self.find_element(*CasinoPageLocatorsBilbet.HEADER_GAME_BUTTON_2).click()
        self.deposit_popup_close()
        print("aviator button success")
        #проверка кнопки скачивания приложения в хедере сайта

    def header_android_button(self):
        assert self.is_element_present(*CasinoPageLocatorsBilbet.HEADER_ANDROID_BUTTON), "download android button is not"
        print("download android button button success")
        #проверка поиска игр через серч  
          
    def casino_banner_carousel(self):
        self.casino_header_logo_home()
        carousel_casino_button = self.browser.find_element(*CasinoPageLocatorsBilbet.CAROUSEL_BANNERS_BUTTON)
        for _ in range(5):  # Прокрутить 5 раз
            carousel_casino_button.click() 
        print("carousel casino success")    

    def game_main_page(self):
        self.find_element(*GeneralPageLocators.PLAY_MOBILE_CASINO_GAME).click()
        self.deposit_popup_close()
        #self.inside_the_game_button_home()
        #self.deposit_popup_close()
        print("game main page success")

    def footer_socials_buttons(self):
        #просто скроллим до футера, иначе тест не видит все элементы в футере
        app_footer_desktop = self.find_element(*CasinoPageLocatorsBilbet.APP_FOOTER_DESKTOP)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", app_footer_desktop)

        assert self.is_element_present(*CasinoPageLocatorsBilbet.FOOTER_FB_ICON), "FB icon is not"
        facebook_icon_in_footer = self.find_element(*CasinoPageLocatorsBilbet.FOOTER_FB_ICON).get_attribute("href")
        if facebook_icon_in_footer == "https://www.facebook.com/bilbet_official-110957771374578":
            print("Reference FB success")
        else:
            print("Reference FB error")    

        assert self.is_element_present(*CasinoPageLocatorsBilbet.FOOTER_INSTAGRAM_ICON), "INSTA icon is not"
        insta_icon_in_footer = self.find_element(*CasinoPageLocatorsBilbet.FOOTER_INSTAGRAM_ICON).get_attribute("href")
        if "https://www.instagram.com/bilbet_official" in insta_icon_in_footer:
            print("Reference instagram success")
        else:
            print("Reference instagram error")

        assert self.is_element_present(*CasinoPageLocatorsBilbet.FOOTER_TELEGRAM_ICON), "TELEGA icon is not"
        telega_icon_in_footer = self.find_element(*CasinoPageLocatorsBilbet.FOOTER_TELEGRAM_ICON).get_attribute("href")
        if "https://t.me/bilbet_official" in telega_icon_in_footer:
            print("Reference TELEGA success")
        else:
            print("Reference TELEGA error")        
       
    # def casino_header_search(self):
    #     search_element_click = self.browser.find_element(*CasinoPageLocatorsBilbet.HEADER_SEARCH_CASINO_GAME)
    #     search_element_click.click()
    #     self.game_container_for_popular_success_open()

    #     self.input_search_game_name.send_keys("te")
    #     assert self.is_element_present(*CasinoPageLocatorsBilbet.USER_CASINO_SEARCH_ERROR), 'error casino search is not'

    #     self.input_search_game_name.send_keys("Royal Coins 2: Hold and Win")
        
    #     playng_search_game_mobile = self.is_element_present(*GeneralPageLocators.PLAY_MOBILE_CASINO_GAME)
    #     if playng_search_game_mobile == True:
    #         self.browser.find_element(*GeneralPageLocators.PLAY_MOBILE_CASINO_GAME).click()
    #     #time.sleep(3)
    #     self.deposit_popup_close()

    #     #self.game_container_success_open()
    #     print("casino header search success")
    #     time.sleep(3)
        
