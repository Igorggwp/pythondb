def pais(mydb):
    mycursor = mydb.cursor()

    mycursor.execute("INSERT INTO pais (nome_pais) VALUES ('Brasil')")
    mydb.commit()

    mycursor.close()