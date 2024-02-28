import requests
import time
import yaml
from .get_token import GetToken

class CreateTransction(GetToken): 
    
    def create_manual_transaction_for_kassma(self):

        with open("config.yaml") as f:
            config = yaml.load(f, Loader=yaml.FullLoader)


        url = config['url_for_deposit_create']
        username = config['username_for_kassma']
        password = config['password_for_kassma']

        token = CreateTransction.get_token(username, password)

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
        
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        if response.status_code == 200:
            
            return transaction_id
        else:
            print(data, f"Не удалось выполнить запрос. Код состояния: {response.status_code}")
            return None    


