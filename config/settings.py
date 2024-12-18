from db.settings import conn

# ========================================================
# Carrega parametros genericos da aplicação
# ========================================================

cursor = conn.cursor()
cursor.execute("select valor from sc_param where codigo = 'NEGOCIARE-CLIENTID'")
valor = cursor.fetchone()
ClienteId = int(valor[0])

cursor.execute("select valor from sc_param where codigo =  'NEGOCIARE-CLIENTSECRET'")
valor = cursor.fetchone()
SecretKey = valor[0]

cursor.execute("select valor from sc_param where codigo =  'NEGOCIARE-SHA1'")
valor = cursor.fetchone()
Sha1Key = valor[0]

cursor.execute("select valor from sc_param where codigo =  'NEGOCIARE-TOKEN'")
valor = cursor.fetchone()
Token_endpoint = valor[0]   



