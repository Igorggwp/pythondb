from faker import Faker
import random

def entrada_produto(mydb):
    mycursor = mydb.cursor()
    info = Faker()

    for _ in range(1):
        id_produto = random.randint(1, 7000000)
        data_entrada = info.date_this_year()
        mycursor.execute("INSERT INTO entrada_produto (id_produto, data_entrada) VALUES (%s, %s)",
                        (id_produto, data_entrada))
        mydb.commit()

    mycursor.close()