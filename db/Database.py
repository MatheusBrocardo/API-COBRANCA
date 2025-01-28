import cx_Oracle
import os
cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_21_3")
SringConnect = f"{os.getenv('OracleUser')}/{os.getenv('OraclePass')}@{os.getenv('OracleAdress')}/{os.getenv('OracleOwner')}"
conn = cx_Oracle.connect(SringConnect)




