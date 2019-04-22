jogadores = list()
total_gols = 0

digitar_valores = str(input('Deixe vazio para carregar a lista preenchida para testar'))
if not digitar_valores:
    jogadores = [{'nome': 'Marta', 'gols': [3, 3, 4, 2], 'total': 12},
                 {'nome': 'Formiga', 'gols': [2, 4, 1], 'total': 19},
                 {'nome': 'Bete', 'gols': [1, 2, 0], 'total': 22},
                 {'nome': 'Clara', 'gols': [1, 3], 'total': 26}]
else:
    """ # NOTE: here be dragons. Dictionaries can be LINKED and NOT COPIED.
        When your put a dictionary into a list, be careful because dictionaries can be linked. So changing one will change the other.
        To avoid this you can write your code in 2 forms:
            1 - Declare a dictionary into the loop, put it into your list (using copy() function is optional but recommended) and delete it after.
                the list.
                while True:
                    your_dict = dict()
                    feed you_dict
                    your_list.append(your_dict)
                    del(your_dict)

            2 - Declare a dictionary outside the loop, put it into list using copy() functions, and clear it after. Clear maybe optional,
                but recommended.
                your_dict()
                while True:
                    feed your dict
                    your_list.append(your_dict.copy())
                    your_dict.clear()
    """
    # jogador = dict()
    while True:
        jogador = dict()
        jogador['nome'] = str(input('Nome do Jogador: '))
        partidas_disputadas = int(input(f'Quantas partidas o jogaor {jogador["nome"]} disputou? '))
        jogador['gols'] = list()
        for partida in range(0, partidas_disputadas):
            jogador['gols'].append(int(input(f'Quantos gols foram marcados na partida {partida + 1}? ')))

            # total_gols += jogador['gols'][partida]
        # jogador['total'] = total_gols
        jogador["total"] = sum(jogador["gols"])

        jogadores.append(jogador.copy())
        del(jogador)
        while True:
            finaliza = str(input('Deseja continuar? [S/N] ')).strip().upper()
            if (finaliza) or (finaliza in 'SN'):
                break
            print('Opção inválida.')

        if finaliza == 'N':
            break

while True:
    print(f'{"Cod":<5}{"Nome":<15}{"Gols":<15}{"Total":<4}')
    print('-' * 41)

    for codigo, artilheiro in enumerate(jogadores):
        print(f'{codigo + 1:<5}{artilheiro["nome"]:<15}{str(artilheiro["gols"]):<15}{artilheiro["total"]:<4}')

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
        print('-' * 41)

    else:
        break
print('-' * 50)
print(f'{"PROGRAMA ENCERRADO":^50}')
