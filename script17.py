frase = "Eu amo comer chocolate quando posso"


print("Contagem direta: ", frase.count('amo'))


contador = 0
lista_termos = frase.split()
for termo in lista_termos:
    if termo == 'amo':
        contador += 1

print("Contagem correta: ", contador)