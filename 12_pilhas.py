# Palíndromo: é um texto que, quando lido de trás pra frente, mantem o mesmo contéudo (Desprezando acentos e espacamento)

# texto = "SOCORRAM-ME, SUBI NO ONIBUS EM MARROCOS"

texto = "BATATINHA QUANDO NASCE ESPALHA RAMA PELO CHÃO"

pilha = []

# Percurso do palindromo em ordem inversa, colocando cada letra na lista de trás pra frente

#for x in range (len(palindromo), -1, -1, -1):
#   lista.append (palindromo[x])

#print(lista)

for letra in (texto):
    pilha.append (letra)    # append () sempre acrescenta por ULTIMO.

#pilha.insert (10, 'y')
#pilha.insert (19, 'g')
#pilha.insert (6, 'ç')

inverso = ""

# Remoção de elementos em posições que não são a final
# del pilha [11] # Remove a posição desejada.
# del pilha [21]
# del pilha [8]
# del pilha [25]

# Retira cada letra da lista, de trás pra frente, e coloca no inverso
while len(pilha) > 0:
    inverso += pilha.pop() #  pop() retira sempre o ULTIMO elemento

print(inverso)

# PILHA
# A pilha  é um tipo abstrado de dado (TAD) que permite a entrada e a saída de dados apenas na sua extremidade final.
# Como consequencia, ela segue a regre LIFO (Last in, first out - Ultimo a entrar, primeiro a sair).
# E tem acesso limitado aos seus elementos.
# Pilha 