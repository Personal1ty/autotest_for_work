from selenium.webdriver.common.by import By

class GeneralPageLocators():
    CLOSE_MOBILE_DEP_POPUP = (By.CSS_SELECTOR, '[class="user-modal__close"]')
    PLAY_MOBILE_CASINO_GAME = (By.CSS_SELECTOR, '[class="user-casino-game-card__image"]')
    PLAYNG_DESKTOP_CASINO_GAME = (By.CSS_SELECTOR, '[class="game-card-overlay__btn"]')
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BACKET = (By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')

class LoginPageLocatorsBilbet():
    CLICK_LOGIN_BUTTON = (By.CSS_SELECTOR, '[class="account__login account__btn"]')
    INPUT_EMAIL = (By.CSS_SELECTOR, '[testid="login-email"]')
    INPUT_PASS = (By.CSS_SELECTOR, '[testid="login-password"]')
    CLICK_AUTHORIZATION_BUTTON = (By.CSS_SELECTOR, '[class="submit-button auth-content-form__submit"]')
    LOGIN_ERROR = (By.CSS_SELECTOR, '[testid="login-email-error"]')
    PASS_ERROR = (By.CSS_SELECTOR, '[testid="login-password-error"]')
    INPUT_PHONE = (By.CSS_SELECTOR,'[testid="registration-phone"]')
    INPUT_PASS_PHONE = (By.CSS_SELECTOR, '[testid="login-password"]')
    PHONE_ERROR = (By.CSS_SELECTOR, '[testid="registration-phone-error"]')
    FORGOT_PASSWORD = (By.CSS_SELECTOR, '[class="form-item__forgot-password"]')
    CLICK_PHONE = (By.CSS_SELECTOR, '[class="form-type-tabs__tab"]')
    CLICK_EMAIL = (By.CSS_SELECTOR, '[class="form-type-tabs__tab"]')
    
class RegisterPageLocatorsBilbet():
    CLICK_REGISTER_BUTTON = (By.CSS_SELECTOR, '[class="account__register account__btn"]')

    ACCOUNT_CURRENCY_SELECT = (By.CSS_SELECTOR, '[class="currency-select__inner"]')
    ACCOUNT_CURRENCY_INR = (By.CSS_SELECTOR, '.currency-select-popper__item:nth-child(2)') 
    ACCOUNT_CURRENCY_UZS = (By.CSS_SELECTOR, '.currency-select-popper__item:nth-child(3)') 
    ACCOUNT_CURRENCY_BDT = (By.CSS_SELECTOR, '.currency-select-popper__item:nth-child(4)')

    REG_WELCOME_BONUS = (By.CSS_SELECTOR, '[class="registration-bonus__content"]')
    REG_WELCOME_BONUS_CASINO = (By.CSS_SELECTOR, '.registration-bonus:nth-child(1)')
    REG_WELCOME_BONUS_SPORT = (By.CSS_SELECTOR, '.registration-bonus:nth-child(2)')
    REG_WELCOME_BONUS_PROMOCODE = (By.CSS_SELECTOR, '.registration-bonus:nth-child(3)')
    REG_WELCOME_BONUS_CLICK_CASINO = (By.CSS_SELECTOR, '[class="registration-bonus__content"]')

    INPUT_LOGIN = (By.CSS_SELECTOR, '[testid="registration-email"]')
    INPUT_PASS = (By.CSS_SELECTOR, '[testid="registration-password"]')

    REGISTER_EMAIL_ERROR = (By.CSS_SELECTOR, '[testid="registration-email-error"]')
    REGISTER_PASS_ERROR = (By.CSS_SELECTOR, '[testid="registration-password-error"]')

    CLICK_CREATE_ACCOUNT = (By.CSS_SELECTOR, '[testid="registration-submit-btn"]')
    REGISTRATION_POPUP = (By.CSS_SELECTOR, '[class="registration-popup__title"]')
    
class CasinoPageLocatorsBilbet():
    APP_HEADER_LOGO = (By.CSS_SELECTOR, '[class="app-header__logo"]')
    INPUT_DEP = (By.CSS_SELECTOR, '[class="account__deposit-btn"]')
    VERIFICATION_POPUP = (By.CSS_SELECTOR, '[class="mail-verification__close"]')
    HEADER_AVIATOR_BUTTON = (By.CSS_SELECTOR, '[class="app-header__action app-header__action--aviator"]')
    HEADER_ANDROID_BUTTON = (By.CSS_SELECTOR, '[class="app-header-android-btn"]')
    HEADER_SEARCH_CASINO_GAME = (By.CSS_SELECTOR, '.casino-menu-header__icon:nth-child(4)')
    INPUT_SEARCH_CASINO_GAME = (By.CSS_SELECTOR, '[class="user-casino-search__input"]')
    CHECK_GAME_CONTAINER_FOR_POPULAR = (By.CSS_SELECTOR, '[class="user-casino-games__section"]')