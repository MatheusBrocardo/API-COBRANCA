import requests
import json
from datetime import datetime, timedelta
from config import settings
from typing import Optional

class TokenManeger:
    def __init__(self):
        self._token: Optional[str] = None
        self._token_type: Optional[str] = None
        self._expiration: Optional[datetime] = None
        self._url = settings.Token_endpoint 

    def get_token(self) -> str:

        if self._token is None or self._is_token_expired():
            self._generate_token()
        return f"{self._token_type}{' '}{self._token}"

    def _generate_token(self) -> None:
        
        payload = {
            "client_id": settings.ClienteId,
            "client_secret": settings.SecretKey
        }

        headers = {'Content-Type': 'application/json'}

        try:
            response = requests.post(self._url, data=json.dumps(payload), headers=headers)
            response.raise_for_status()

            data = response.json()
            self._token = data['token']
            self._token_type = data['token_type']
            self._expiration = datetime.now() + timedelta(hours=1)

        except requests.RequestException as e:
            print('Erro')
            raise
        except KeyError as e:
            print('Erro')
            raise

    def _is_token_expired(self) -> bool:
        return datetime.now() >= self._expiration



    




    


