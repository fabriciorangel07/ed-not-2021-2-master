# Palíndromo: é um texto que, quando lido de trás pra frente, mantem o mesmo contéudo (Desprezando acentos e espacamento)

palindromo = "SOCORRAM-ME, SUBI NO ONIBUS EM MARROCOS"

lista = []

# Percurso do palindromo em ordem inversa, colocando cada letra na lista de trás pra frente

#for x in range (len(palindromo), -1, -1, -1):
#   lista.append (palindromo[x])

#print(lista)

for letra in (palindromo):
    lista.append (letra)

inverso = ""

# Retira cada letra da lista, de trás pra frente, e coloca no inverso
while len(lista) > 0:
    inverso += lista.pop() #  pop() retira sempre o ULTIMO elemento

print(inverso)