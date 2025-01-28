import requests
from controllers import Token
from config import settings

DadosToken = Token.TokenManeger()


def envia_cobranca(PayloadRequisicao):

    headers = {
        'Content-Type': 'application/json',
        'Authorization': DadosToken.get_token()
    }

    payload = PayloadRequisicao

    print(payload)

    # response = requests.request("POST", url, headers=headers, data=payload)

    

    

