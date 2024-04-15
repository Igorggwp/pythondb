from faker import Faker

def fornecedor(mydb):
    mycursor = mydb.cursor()
    info = Faker('pt_BR')

    for _ in range(5):
        nome_fornecedor = info.company()
        cnpj_fornecedor = info.cnpj()
        email_fornecedor = info.email()
        active = info.boolean()

        mycursor.execute("INSERT INTO fornecedor (nome_fornecedor, cnpj_fornecedor, email_fornecedor, active) "
                         "VALUES (%s, %s, %s, %s)",
                         (nome_fornecedor, cnpj_fornecedor, email_fornecedor, active))
        mydb.commit()

        id_fornecedor = mycursor.lastrowid
        telefone = info.phone_number()

        mycursor.execute("INSERT INTO telefone (telefone, id_fornecedor) VALUES (%s, %s)",
                         (telefone, id_fornecedor))
        mydb.commit()

    mycursor.close()
