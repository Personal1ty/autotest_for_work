import requests
import yaml
class GetToken():
    def get_token(email, password):
        
        with open("config.yaml") as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
 
        url = config['url_for_auth_predprod']

        payload = {
            'email': email,
            'password': password
        }
        headers = {
            'Content-Type': 'application/json'
        }

        

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            token = data.get('access_token')
            
            if token:
                return token
            else:
                print("Токен не найден в ответе.")
                return None
        else:
            print(f"Не удалось выполнить запрос. Код состояния: {response.status_code}")
            return None