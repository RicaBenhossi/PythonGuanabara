def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} marcou {gols} gol(s) no campeonato.')


jogador = str(input('Nome do jogador: ')).strip()
gols_marcados = str(input('Quantos gols foram marcados? '))
if gols_marcados.replace('.', '', 1).isnumeric():
    gols_marcados = int(float(gols_marcados))
else:
    gols_marcados = 0

if not jogador:
    ficha(gols=gols_marcados)
else:
    ficha(jogador, gols_marcados)
