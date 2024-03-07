import requests


class AuthTokenProvider:
    @staticmethod
    def get_token(payload, auth_url):
        try:
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.post(auth_url, json=payload, headers=headers)
            response.raise_for_status()  # Проверка успешности запроса

            data = response.json()
            
            if data:
                return data
            else:
                print("Токен не найден в ответе.")
                return None
        except requests.RequestException as e:
            print(f"Ошибка при выполнении запроса: {e}")
            return None