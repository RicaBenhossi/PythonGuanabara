jogador = dict()
total_gols = 0

jogador['nome'] = str(input('Nome do Jogador: '))
partidas_disputadas = int(input(f'Quantas partidas o jogaor {jogador["nome"]} disputou? '))
jogador['gols'] = list()
for partida in range(0, partidas_disputadas):
    jogador['gols'].append(int(input(f'Quantos gols foram marcados na partida {partida + 1}? ')))
    total_gols += jogador['gols'][partida]
jogador['total'] = total_gols

print('-' * 50)
print(jogador)
print('-' * 50)

for k, v in jogador.items():
    print(f'o campo {k} tem valor {v}.')
print('-' * 50)
print('Loop com ENUMERATE')
print(f'O Jogador {jogador["nome"]} dispoutou {len(jogador["gols"])} partidas.')
for jogo, gols in enumerate(jogador['gols']):
    print(f'\t=> Na partida {jogo + 1} foi(ram) marcado(s) {gols} gol(s).')
print(f'Foi(ram) marcado(s) no total {jogador["total"]} gol(s).')
print('-' * 50)
print('Loop com RANGE')
print(f'O Jogador {jogador["nome"]} disputou {len(jogador["gols"])} partidas.')
for jogo in range(0, len(jogador['gols'])):
    print(f'\t=> Na partida {jogo + 1} foi(ram) marcado(s) {jogador["gols"][jogo]} gol(s).')
print(f'Foi(ram) marcado(s) no total {jogador["total"]} gol(s).')
