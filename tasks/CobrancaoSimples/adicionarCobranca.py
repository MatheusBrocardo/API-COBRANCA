from db import Database
from models import ModeloAdicionarCobranca
from controllers import AdicionaCobranca

def carrega_titulos():

    cursor = Database.conn.cursor()
    cursor.execute("select * from v_sync_cobranca")
    fila_clientes = cursor.fetchall()
    
    for r in fila_clientes:
        AdicionaCobranca.envia_cobranca(ModeloAdicionarCobranca.monta_titulos(r[0],r[1],r[2]))
        # cursor.callproc('fn_sync_cobranca_utl.grava_ret_envio_cobranca',[r[0],r[1],])
        # cursor.callproc('fn_sync_cobranca_utl.ler_retorno_envio_banco',[r[0],r[1],])

def consulta_titulos():
    cursor = Database.conn.cursor()
    cursor.execute("select * from v_sync_cobranca")
    fila_clientes = cursor.fetchall()
    
    for r in fila_clientes:
        cursor.callproc('fn_sync_cobranca_utl.ler_retorno_envio_banco',[r[0],r[1],])
