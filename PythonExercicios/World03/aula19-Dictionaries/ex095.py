jogadores = list()
total_gols = 0

digitar_valores = str(input('Deixe vazio para carregar a lista preenchida para testar'))
print(f'tes{digitar_valores}te')
if not digitar_valores:
    jogadores = [{'nome': 'Marta', 'gols': [3, 3, 4, 2], 'total': 12},
                 {'nome': 'Formiga', 'gols': [2, 4, 1], 'total': 19},
                 {'nome': 'Bete', 'gols': [1, 2, 0], 'total': 22},
                 {'nome': 'Clara', 'gols': [1, 3], 'total': 26}]
else:
    while True:
        jogador = dict()
        jogador['nome'] = str(input('Nome do Jogador: '))
        partidas_disputadas = int(input(f'Quantas partidas o jogaor {jogador["nome"]} disputou? '))
        jogador['gols'] = list()
        for partida in range(0, partidas_disputadas):
            jogador['gols'].append(int(input(f'Quantos gols foram marcados na partida {partida + 1}? ')))

            total_gols += jogador['gols'][partida]
        jogador['total'] = total_gols
        jogadores.append(jogador)
        del(jogador)
        while True:
            finaliza = str(input('Deseja continuar? [S/N] ')).strip().upper()
            if (not finaliza) or (finaliza not in 'SN'):
                print('Opção inválida.')
            else:
                break

        if finaliza == 'N':
            break

print(f'{"Cod":<5}{"Nome":<15}{"Gols":<15}{"Total":<4}')
print('-' * 41)

for codigo, artilheiro in enumerate(jogadores):
    print(f'{codigo + 1:<5}{artilheiro["nome"]:<15}{str(artilheiro["gols"]):<15}{artilheiro["total"]:<4}')

while True:
    print('-' * 50)
    while True:
        menu_jogador = input('Deseja ver os gols de qual jogador(a)? [0 - sair] ')
        if menu_jogador.isnumeric() and ((int(menu_jogador) <= len(jogadores) > 0)):
            menu_jogador = int(menu_jogador)
            break
        else:
            print('Opção inválida.')

    print()
    if menu_jogador != 0:
        media_gols_partida = float()
        menu_jogador -= 1
        print(f'Levntamento do jogador(a) {jogadores[menu_jogador]["nome"]}')
        for partida, gols in enumerate(jogadores[menu_jogador]["gols"]):
            print(f'\tNa partida {partida + 1} marcou {gols} gol(s).')
            media_gols_partida += gols
        media_gols_partida = media_gols_partida / len(jogadores[menu_jogador]['gols'])
        print(f'Média de {media_gols_partida:.1f} gol(s) por partida.')

    else:
        break
print('-' * 50)
print(f'{"PROGRAMA ENCERRADO":^50}')
