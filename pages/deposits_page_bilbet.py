from .base_page import BasePage
from .locators import CasinoPageLocatorsBilbet
from .locators import GeneralPageLocators
from .locators import CasinoPageDepositLocatorsBilbet
import time
import logging
from selenium.webdriver.common.by import By
import json
import requests
import time
from requests.auth import HTTPBasicAuth

class CasinoDepositsPage(BasePage):

    def deposit_popup_close(self):  #временный метод, после связи удалить
        time.sleep(5)
        deposit_popup = self.is_element_present(*GeneralPageLocators.CLOSE_MOBILE_DEP_POPUP)
        if deposit_popup == True:
           return self.find_element(*GeneralPageLocators.CLOSE_MOBILE_DEP_POPUP).click()
        else:
            print("there is money in the account") 
        print("deposit popup close") 

    def get_token(username, password):
        url = '' 
        payload = {
            'name': username,
            'password': password
        }
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            array = data.get('data')
            token = array['token']
            if token:
                return token
            else:
                print("Токен не найден в ответе.")
                return None
        else:
            print(f"Не удалось выполнить запрос. Код состояния: {response.status_code}")
            return None



    def create_manual_transaction_for_kassma(self):
        url = ""
        username = ''
        password = ''

        token = self.get_token(username, password)

        time_value = time.time()
        transaction_id = int(time_value)

        payload = {
        "type": 1,
        "activate": False,
        "currency_code": "INR",
        "wallet_type": "paytm",
        "transaction_id": f"{transaction_id}",
        "amount": "500",
        "exchange_identifier": "1"
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }
        
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        if response.status_code == 200:
            print("Кошелек успешно создан")
            return transaction_id
        else:
            print(data, f"Не удалось выполнить запрос. Код состояния: {response.status_code}")
            return None
        
    def open_deposit_popup(self):
        open_deposit_popup = self.browser.find_element(*CasinoPageLocatorsBilbet.INPUT_DEP)
        open_deposit_popup.click()

    def select_paytm(self):
        open_deposit_popup = self.browser.find_element(*CasinoPageDepositLocatorsBilbet.SELECT_PAYTM)
        open_deposit_popup.click()

    def input_amount(self):
        input_amount = self.browser.find_element(*CasinoPageDepositLocatorsBilbet.SELECT_DEPOSIT_AMOUNT)       
        input_amount.click()

    def click_pay_button(self):
        click_pay_button = self.browser.find_element(*CasinoPageDepositLocatorsBilbet.PAY_BUTTON)       
        click_pay_button.click()

    def input_transaction_id(self):
        input_transaction_id = self.browser.find_element(*CasinoPageDepositLocatorsBilbet.INPUT_TRANSACTION_ID)
        input_transaction_id.send_keys(self.create_manual_transaction_for_kassma())       
     
