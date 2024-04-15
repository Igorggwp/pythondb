import mysql.connector
from categoria import categoria
from pais import pais
from estado import estado
from cidade import cidade
from endereco import endereco
from fornecedor import fornecedor
from telefone import telefone
from produto import produto
from entrada_produto import entrada_produto
from saida_produto import saida_produto

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="tradeon"
)

def menu():
    print("Escolha uma opção para popular a tabela:")
    print("1. Categoria")
    print("2. Pais")
    print("3. Estado")
    print("4. Cidade")
    print("5. Endereço")
    print("6. Fornecedor")
    print("7. Telefone")
    print("8. Produto")
    print("9. Entrada de Produto")
    print("10. Saída de Produto")
    print("0. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        categoria(mydb)
    elif opcao == "2":
        pais(mydb)
    elif opcao == "3":
        estado(mydb)
    elif opcao == "4":
        cidade(mydb)
    elif opcao == "5":
        endereco(mydb)
    elif opcao == "6":
        fornecedor(mydb)
    elif opcao == "7":
        telefone(mydb)
    elif opcao == "8":
        produto(mydb)
    elif opcao == "9":
        entrada_produto(mydb)
    elif opcao == "10":
        saida_produto(mydb)
    elif opcao == "0":
        print("Encerrando...")
        return
    else:
        print("Erro.")
    
    menu()
menu()

mydb.close()