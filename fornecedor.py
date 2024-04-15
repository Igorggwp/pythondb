from faker import Faker
import random

def fornecedor(mydb):
    mycursor = mydb.cursor()
    info = Faker()

    fornecedores = []
    for _ in range(5):
        nome_fornecedor = info.company()
        cnpj_fornecedor = info.cnpj()
        email_fornecedor = info.email()
        active = info.boolean()
        fornecedores.append((nome_fornecedor, cnpj_fornecedor, email_fornecedor, active))

    for fornecedor in fornecedores:
        sql = "INSERT INTO fornecedor (nome_fornecedor, cnpj_fornecedor, email_fornecedor, active, id_endereco) " \
            "VALUES (%s, %s, %s, %s, %s)"
        val = fornecedor + (random.randint(1, 10),)
        mycursor.execute(sql, val)
        mydb.commit()

    mycursor.close()
    return fornecedores 