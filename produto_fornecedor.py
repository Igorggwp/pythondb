import random

def produto_fornecedor(mydb):
    mycursor = mydb.cursor()

    mycursor.execute("SELECT MIN(id_produto), MAX(id_produto) FROM produto")
    produtoMin, produtoMax = mycursor.fetchone()

    mycursor.execute("SELECT MIN(id_fornecedor), MAX(id_fornecedor) FROM fornecedor")
    fornecedorMin, fornecedorMax = mycursor.fetchone()

    for _ in range(1):
        id_produto = random.randint(produtoMin, produtoMax)
        id_fornecedor = random.randint(fornecedorMin, fornecedorMax)
        mycursor.execute("INSERT INTO produto_fornecedor (id_produto, id_fornecedor) VALUES (%s, %s)",
                         (id_produto, id_fornecedor))

    mydb.commit()
    mycursor.close()