from faker import Faker
from fornecedor import fornecedor
import random

def telefone(mydb):
    mycursor = mydb.cursor()
    info = Faker()

    fornecedores = fornecedor(mydb) 

    for _ in range(10):
        telefone = info.phone_number()
        id_fornecedor = random.choice(fornecedores)[0]
        sql = "INSERT INTO telefone (telefone, id_fornecedor) VALUES (%s, %s)"
        val = (telefone, id_fornecedor)
        mycursor.execute(sql, val)
        mydb.commit()

    mycursor.close()