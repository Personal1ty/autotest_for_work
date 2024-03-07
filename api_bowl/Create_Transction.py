import requests
import time
from .Auth_Token_Provider import AuthTokenProvider
from autotest_for_work.pages.base_page import BasePage

class CreateTransction(): 
    @staticmethod
    def create_manual_transaction_for_kassma(username, password, auth_url):
        try:
            payload = {
               "name": username,
               "password": password
            }
            config = BasePage.load_config()
            deposit_url = config['url_for_deposit_create'] #вот эта штука может не работать
            
            auth_response = AuthTokenProvider.get_token(payload, auth_url)
            array = auth_response.get('data')
            token = array['token'] 
            if token:
                time_value = time.time()
                transaction_id = "00" + str(int(time_value))

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
                
                response = requests.post(deposit_url, json=payload, headers=headers)
                response.raise_for_status()  # Проверка успешности запроса

                data = response.json()
                if response.status_code == 200:
                    return transaction_id
                else:
                    print(data, f"Не удалось выполнить запрос. Код состояния: {response.status_code}")
                    return None    
        except Exception as e:
            print(f"Ошибка при создании транзакции: {e}")
            return None   


