from faker import Faker
from estado import estados_brasil
import random

def cidade(mydb):
    mycursor = mydb.cursor()
    info = Faker()

    estados = estados_brasil()

    for _ in range(10):
        nome_cidade = info.city()
        estado_id = random.randint(1, len(estados))
        mycursor.execute("INSERT INTO cidade (nome_cidade, estado_id) VALUES (%s, %s)",
                         (nome_cidade, estado_id))
        mydb.commit()
    
    mycursor.close()