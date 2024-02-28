import requests
import yaml
from .get_token import GetToken


class UpdatePosition(GetToken): 

    def update_payment_position(self):

        with open("config.yaml") as f:
            config = yaml.load(f, Loader=yaml.FullLoader)


        url = config['url_for_update_position']
        email = config['admin_login_for_bilbet']
        password = config['admin_pass_for_bilbet']

        token = UpdatePosition.get_token(email, password)


        payload = {
            "name": "PayTM",
            "position": 1,
            "categories": [5],
            "sort_type": "POSITION",
            "currency": "INR",
            "enabled": True,
            "payment_systems": [
                {
                    "payment_system_id": 1,
                    "probability": 0
                }
            ]
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }
        
        response = requests.patch(url, json=payload, headers=headers)
        data = response.json()
        if response.status_code == 200:
            
            return print(data)
        else:
            print(data, f"Не удалось выполнить запрос. Код состояния: {response.status_code}")
            return None    
        

      