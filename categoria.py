from faker import Faker

def categoria(mydb):
    mycursor = mydb.cursor()
    info = Faker()

    cat = [
        "Eletrônicos", "Roupas", "Alimentos", "Esportes", "Decoração",
        "Móveis", "Brinquedos", "Tecnologia", "Viagens", "Instrumentos Musicais",
        "Higiene", "Casa e Jardim", "Arte e Artesanato", "Animais de Estimação", "Moda Íntima",
        "Ferramentas", "Material de Escritório", "Produtos Químicos", "Peças Automotivas", "Produtos de Limpeza"
    ]

    for nome_categoria in cat:
        desc_categoria = info.sentence()
        active = info.boolean()

        mycursor.execute("INSERT INTO categoria (nome_categoria, desc_categoria, active) VALUES (%s, %s, %s)",
                          (nome_categoria, desc_categoria, active))

    mydb.commit()

    mycursor.close()