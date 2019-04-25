from random import randint


def Sorteia(lista):
    for x in range(0, 5):
        lista.append(randint(0, 5))
    print(lista)


def SomaPar(numeros):
    soma_par = 0
    Sorteia(numeros)
    for num in numeros:
        if num % 2 == 0:
            soma_par += num
    print(soma_par)


print('*' * 40)
lista_numeros = list()
# Sorteia(lista_numeros)
SomaPar(lista_numeros)
