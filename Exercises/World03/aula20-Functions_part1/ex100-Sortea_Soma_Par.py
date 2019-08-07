from random import randint
from time import sleep


def Sorteia(lista):
    print('*' * 40)
    print('Sorteando 5 números aleatório entre 1 e 10')
    for x in range(0, 5):
        lista.append(randint(1, 10))
        print(lista[x], end=' ', flush=True)
        sleep(0.5)
    print('-' * 40)
    print(f'A Lista completa é {lista}')


def SomaPar(lista):
    soma_par = 0
    print('*' * 40)
    for num in lista:
        if num % 2 == 0:
            soma_par += num
    print(f'A Soma dos elementos pares da lista {lista} é {soma_par}.')


lista_numeros = list()
Sorteia(lista_numeros)
SomaPar(lista_numeros)
