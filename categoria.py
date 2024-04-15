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

    categorias = []
    for nome_categoria in cat:
        desc_categoria = info.sentence()
        active = info.boolean()
        categorias.append((nome_categoria, desc_categoria, active))

    for categoria in categorias:
        sql = "INSERT INTO categoria (nome_categoria, desc_categoria, active) VALUES (%s, %s, %s)"
        val = categoria
        mycursor.execute(sql, val)

    mydb.commit()

    mycursor.close()