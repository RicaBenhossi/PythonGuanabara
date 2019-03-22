from random import randint
from time import sleep

print('=' * 50)
print(f'{"JOGOS DA MEGA SENA":^50}')
print('=' * 50)

jogos = list()
qtd_jogos = int(input('Quantos jogos deseja gerar? '))
print(f'\nSorteando {qtd_jogos} jogos\n')

for x in range(0, qtd_jogos):
    sleep(0.8)
    jogos.append(list())
    while len(jogos[x]) < 6:
        while True:
            numero = randint(1, 60)
            if numero not in jogos[x]:
                jogos[x].append(numero)
                break
        jogos[x].sort()
    print(f'Jogo {x + 1}: {jogos[x]}')
print(f'\n\n{"BOA SORTE!":^50}')
