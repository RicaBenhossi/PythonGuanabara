from random import randint

jogadas = dict()
maior = 0
vencedor = ''
for jogador in range(1, 5):
    jogadas['jogador' + str(jogador)] = randint(1, 7)
    if jogadas['jogador' + str(jogador)] > maior:
        maior = jogadas['jogador' + str(jogador)]
        vencedor = 'jogador' + str(jogador)
    print(jogadas.items())

print(vencedor)
print(maior)

ranking = dict()
ranking[jogador] = jogadas[jogador]
del jogadas[jogador]
for k, v in jogadas.items():
