import requests
class Webhook:
        @staticmethod
        def send(url, text):
            payload = {
                'content': f'{text}',
            }

            # Webhook'a POST isteği gönderin
            response = requests.post(url=url, data=payload)