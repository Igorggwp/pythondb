from faker import Faker
import random

def saida_produto(mydb):
    mycursor = mydb.cursor()
    info = Faker()

    for _ in range(1):
        id_produto = random.randint(1, 7000000)
        quantidade = random.randint(1, 100)
        data_saida = info.date_this_year()
        mycursor.execute("INSERT INTO saida_produto (id_produto, quantidade, data_saida) VALUES (%s, %s, %s)",
                        (id_produto, quantidade, data_saida))
        mydb.commit()

    mycursor.close()