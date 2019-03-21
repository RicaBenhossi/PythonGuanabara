from random import randint

jogos = list()
qtd_jogos = int(input('Quantos jogos deseja gerar? '))

for x in range(0, qtd_jogos):
    while len(jogos[x] <= 6):
        jogos[x].append(randint(1, 10, 1))

print(jogos)
