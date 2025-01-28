from db import Database
from models.Inadimplencia import AdicionarTitulos
from controllers.Inadimplencia import 
def carrega_titulos():

    cursor = Database.conn.cursor()
    cursor.execute("select * from v_sync_cobranca")
    fila_clientes = cursor.fetchall()
    
    for r in fila_clientes:

        AdicionaCobranca.envia_cobranca(Inadimplencia.AdicionarTitulos.monta_titulos(r[0],r[1],r[2]))
        # cursor.callproc('fn_sync_cobranca_utl.grava_ret_envio_cobranca',[r[0],r[1],])
        # cursor.callproc('fn_sync_cobranca_utl.ler_retorno_envio_banco',[r[0],r[1],])

    







        








    