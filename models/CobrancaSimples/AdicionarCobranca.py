from db import Database
from config import settings
import json

def monta_titulos(id_cobranca,id_api,CodEntidade):

    cursor = Database.conn.cursor()

    cliente_dados = """
            SELECT documento, nome, razao_social, cep, endereco, numero, complemento, 
                cidade, uf, email
            FROM v_sync_cobranca_dados
            WHERE id_cob = :p_id_cob and id_api  = :p_id_api"""

    cliente_contatos = """
            SELECT contato from v_sync_cobranca_contatos where id_cob = :p_id_cob and id_api = :p_id_api"""

    cliente_titulos = """
            SELECT sequencia_titulo,data_vencimento,valor,valor_mora_dia,valor_multa_mes,mensagem,callback_url,id_cob,id_api from v_sync_cobranca_titulos where id_cob = :p_id_cob and id_api = :p_id_api"""

    cursor.execute(cliente_dados,p_id_cob = id_cobranca,p_id_api = id_api)
    dados_cliente = cursor.fetchone()

    cursor.execute(cliente_contatos,p_id_cob = id_cobranca,p_id_api = id_api)
    contatos_lista = [contato[0] for contato in cursor.fetchall()]

    cursor.execute(cliente_titulos,p_id_cob = id_cobranca,p_id_api = id_api)
    dados_titulos_lista = cursor.fetchall()

    cursor.close()

    # Montar o JSON
    result = {
        "cliente": {
            "documento": dados_cliente[0],
            "nome": dados_cliente[1],
            "razao_social": dados_cliente[2] or "",
            "cep": dados_cliente[3],
            "endereco": dados_cliente[4],
            "numero": dados_cliente[5],
            "complemento": dados_cliente[6] or "",
            "cidade": dados_cliente[7],
            "uf": dados_cliente[8],
            "telefones": contatos_lista,
            "email": dados_cliente[9]
        },
        "id_geral": id_api,
        "parcelas": []
    }

    for parcela in dados_titulos_lista:
        parcela_dict = {
            "id_parcela": parcela[0],
            "data_vencimento": parcela[1],
            "valor": float(parcela[2]),
            "mensagem": parcela[5],
            "callback_url": parcela[6]
        }

        # if parcela[3]:  # valor_mora_dia
        #     parcela_dict["valor_mora_dia"] = float(parcela[3])
        #     parcela_dict["valor_multa_mes"] = float(parcela[4])
        # else:
        #     parcela_dict["percentual_juros_mes"] = float(parcela[7])
        #     parcela_dict["percentual_multa"] = float(parcela[8])

        # if parcela[9]:  # desconto_percentual
        #     parcela_dict["desconto_pontualidade"] = {
        #         "percentual": float(parcela[9]),
        #         "data_limite": parcela[10]
        #     }

        result["parcelas"].append(parcela_dict)

    return json.dumps(result, ensure_ascii=False, indent=2)

