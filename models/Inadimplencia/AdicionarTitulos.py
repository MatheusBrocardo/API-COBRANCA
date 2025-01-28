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
            select num_seq_tit_lote,data_vencimento,valor,seq_titulo,id_cob,id_api from v_sync_cobranca_titulos where id_cob = :p_id_cob and id_api = :p_id_api"""

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
        "titulos": []
    }

    for parcela in dados_titulos_lista:
        parcela_dict = {
            "cod_titulo": parcela[0],
            "data_vencimento": parcela[1],
            "valor": float(parcela[2]),
            "numero_parcela": parcela[3]
        }

        result["titulos"].append(parcela_dict)

    return json.dumps(result, ensure_ascii=False, indent=2)

