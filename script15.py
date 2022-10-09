with open("dados13.txt", "r") as arquivo:
    texto = arquivo.read()
    contador = texto.count("Olá Humano")
    print("Total de Olá = ", contador)