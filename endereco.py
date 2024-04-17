from faker import Faker
from estado import estados_brasil
import random

def endereco(mydb):
    mycursor = mydb.cursor()
    info = Faker()

    estados = estados_brasil()
    for _ in range(50000):
        rua = info.street_name()
        numero = info.random_number(digits=3)
        bairro = info.name()
        cidade_id = random.randint(1, 1000000)
        estado_id = random.randint(1, 27)
        pais_id = 1
        active = info.boolean()
        
        mycursor.execute("INSERT INTO endereco (rua, numero, bairro, cidade_id, estado_id, pais_id, active) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (rua, numero, bairro, cidade_id, estado_id, pais_id, active))
    mydb.commit()
        
    mycursor.close()