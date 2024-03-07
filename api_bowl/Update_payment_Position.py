import requests
from .Auth_Token_Provider import AuthTokenProvider
from autotest_for_work.pages.base_page import BasePage

class UpdatePosition:
    @staticmethod
    def update_payment_position(email, password, auth_url):
        try:
            payload = {
               "email": email,
               "password": password
            }
            config = BasePage.load_config()
            update_url = config['url_for_update_position'] #вот эта штука может не работать

            auth_response = AuthTokenProvider.get_token(payload, auth_url)
            token = auth_response.get('access_token')
            if token:
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
                
                response = requests.patch(update_url, json=payload, headers=headers)
                response.raise_for_status()  # Проверка успешности запроса

                data = response.json()
                if response.status_code == 200:
                    return print(data)
                else:
                    print(data, f"Не удалось выполнить запрос. Код состояния: {response.status_code}")
                    return None
        except Exception as e:
            print(f"Ошибка при обновлении позиции: {e}")
            return None    
        

      