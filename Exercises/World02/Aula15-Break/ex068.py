from random import randint
vitorias = 0
while True:
    while True:
        ParOuImpar = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()[0]
        if ParOuImpar in 'IP':
            break
    computador = randint(1, 2)
    jogador = int(input('Digite o seu número: '))
    resultado = 'P' if ((jogador + computador) % 2) == 0 else 'I'
    print(f'Você jogou {jogador} e escolheu {ParOuImpar}')
    print(f'O Computador jogou {computador}.')
    if ParOuImpar == resultado:
        print('PARABÉNS! Você venceu...')
        vitorias += 1
        print('{-:^*40-'.format('Vamos jogar novamente'))
    else:
        print('Que pena. Você perdeu. Jogo encerrado')
        print(f'Você venceu {vitorias} partida(s).')
        break
