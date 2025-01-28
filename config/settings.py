from db import Database

# ========================================================
# Carrega parametros genericos da aplicação
# ========================================================

cursor = Database.conn.cursor()
cursor.execute("select valor from sc_param where codigo = 'NEGOCIARE-CLIENTID'")
valor = cursor.fetchone()
ClienteId = int(valor[0])

cursor.execute("select valor from sc_param where codigo =  'NEGOCIARE-CLIENTSECRET'")
valor = cursor.fetchone()
SecretKey = valor[0]

cursor.execute("select valor from sc_param where codigo =  'NEGOCIARE-SHA1'")
valor = cursor.fetchone()
Sha1Key = valor[0]

cursor.execute("select valor from sc_param where codigo =  'NEGOCIARE-PATH'")
valor = cursor.fetchone()
Path_endpoint = valor[0]   

cursor.execute("select valor from sc_param where codigo =  'NEGOCIARE-RT'")
valor = cursor.fetchone()
_login = valor[0]

cursor.execute("select valor from sc_param where codigo =  'NEGOCIARE-RT1'")
valor = cursor.fetchone()
_addCobranca = valor[0]

cursor.execute("select valor from sc_param where codigo =  'NEGOCIARE-RT2'")
valor = cursor.fetchone()
_consultaCobranca = valor[0]

cursor.execute("select valor from sc_param where codigo =  'NEGOCIARE-RT3'")
valor = cursor.fetchone()
_baixaParcelas = valor[0]

cursor.execute("select valor from sc_param where codigo =  'NEGOCIARE-RT4'")
valor = cursor.fetchone()
_consultaParcelasPagas = valor[0]

cursor.execute("select valor from sc_param where codigo =  'NEGOCIARE-RT5'")
valor = cursor.fetchone()
_consultaAlterasHoje = valor[0]







