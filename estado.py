def estados_brasil():
    return [
        ("Acre", "AC"), ("Alagoas", "AL"), ("Amapá", "AP"), ("Amazonas", "AM"), ("Bahia", "BA"),
        ("Ceará", "CE"), ("Distrito Federal", "DF"), ("Espírito Santo", "ES"), ("Goiás", "GO"),
        ("Maranhão", "MA"), ("Mato Grosso", "MT"), ("Mato Grosso do Sul", "MS"), ("Minas Gerais", "MG"),
        ("Pará", "PA"), ("Paraíba", "PB"), ("Paraná", "PR"), ("Pernambuco", "PE"), ("Piauí", "PI"),
        ("Rio de Janeiro", "RJ"), ("Rio Grande do Norte", "RN"), ("Rio Grande do Sul", "RS"),
        ("Rondônia", "RO"), ("Roraima", "RR"), ("Santa Catarina", "SC"), ("São Paulo", "SP"),
        ("Sergipe", "SE"), ("Tocantins", "TO")
    ]

def estado(mydb):
    mycursor = mydb.cursor()

    for estado in estados_brasil():
        nome_estado, sigla = estado
        mycursor.execute("INSERT INTO estado (nome_estado, sigla, pais_id) VALUES (%s, %s, %s)",
                         (nome_estado, sigla, 1))
        mydb.commit()

    mydb.close()