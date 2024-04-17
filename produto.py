from faker import Faker
import random

def produto(mydb):
    mycursor = mydb.cursor()
    info = Faker()

    for _ in range(1000000):
        nome_produto = info.word()
        desc_produto = info.sentence()
        quant_min = random.randint(1, 100)
        peso_prod = random.uniform(0.1, 50.0)
        perecivel = info.boolean()
        data_validade = info.date_this_decade() if perecivel else None
        valor_unitario = random.uniform(1.0, 100.0)
        valor_venda = random.uniform(1.0, 1000.0)
        id_categoria = random.randint(1, 20)
        quantidade = random.randint(1, 1000)
        
        mycursor.execute("INSERT INTO produto (nome_produto, desc_produto, quant_min, peso_prod, perecivel, " \
            "data_validade, valor_unitario, valor_venda, id_categoria, quantidade) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (nome_produto, desc_produto, quant_min, peso_prod, perecivel,
                         data_validade, valor_unitario, valor_venda, id_categoria, quantidade))
        mydb.commit()

    mycursor.close()

