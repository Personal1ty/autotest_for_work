from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select



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
