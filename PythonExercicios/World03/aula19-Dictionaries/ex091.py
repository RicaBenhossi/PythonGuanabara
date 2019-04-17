from random import randint
from operator import itemgetter
from time import sleep

jogadas = dict()
for jogador in range(1, 5):
    jogadas['jogador' + str(jogador)] = randint(1, 7)

ranking = list()
print('Valores Sorteados:')
for k, v in jogadas.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.6)
print('=' * 50)
print('Ranking:')
ranking = (sorted(jogadas.items(), key=itemgetter(1), reverse=True))
# print(ranking)

for i, v in enumerate(ranking):
    print(f'\t{i + 1} Lugar: {v[0]} com {v[1]} pontos.')
