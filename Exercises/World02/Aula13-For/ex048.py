soma = 0
cont = 0
for x in range(1, 501):
    if ((x % 2 != 0) and (x % 3 == 0)):
        cont += 1
        soma += x
print('A soma dos {} números ímpares múltiplos de 3 de 1 a 500 é {}.'.format(cont, soma))

''' BETTER WAY! '''
soma = 0
cont = 0
for x in range(1, 501, 2):  # Here we already cut the evens.
    if (x % 3 == 0):
        cont += 1
        soma += x
print('A soma dos {} números ímpares múltiplos de 3 se 1 a 500 é {}.'.format(cont, soma))
