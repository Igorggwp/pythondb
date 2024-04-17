import time
import mysql.connector
from categoria import categoria
from pais import pais
from estado import estado
from cidade import cidade
from endereco import endereco
from fornecedor import fornecedor
from produto import produto
from entrada_produto import entrada_produto
from saida_produto import saida_produto
from produto_fornecedor import produto_fornecedor

inicio = time.time()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tradeon"
)
print("Inicio do loop")
produto(mydb)
print("2")
produto(mydb)
print("Fim do loop")

fim = time.time()
segundos = fim - inicio
minutos = segundos / 60

print(f"Tempo total de execução: {minutos:.2f} minutos.")

mydb.close()
