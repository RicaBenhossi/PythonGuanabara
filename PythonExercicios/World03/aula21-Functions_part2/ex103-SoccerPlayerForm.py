def ficha(jogador='<desconhecido>', gols=None):
    if not gols:
        gols = 0
    print(f'O jogador {jogador} marcou {gols} gol(s) no campeonato.')


ficha(str(input('Nome do jogador: ')), str(input('Quantos gols foram marcados? ')))
