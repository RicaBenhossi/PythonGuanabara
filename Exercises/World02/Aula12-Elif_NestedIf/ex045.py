from random import randint

print('JOKENPÔ')
print('-' * 30)
print('0 - PEDRA\n1 - PAPEL\n2 - TESOURA')
computador = randint(0, 2)
print('O Computador já fez a sua escolha.')
player = int(input('Qual a sua escolha? '))
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
if (((computador == 1) and (player == 2)) or ((computador == 2) and (player == 3)) or ((computador == 3) and (player == 1))):
    print('O Computador escolheu {} e você escolheu {}. Você VENCEU.'.format(opcoes[computador], opcoes[player]))
elif (computador == player):
    print('O Computador escolheu {} e você escolheu {}. É um EMPATE.'.format(opcoes[computador], opcoes[player]))
else:
    print('O Computador escolheu {} e você escolheu {}. Você PERDEU.'.format(opcoes[computador], opcoes[player]))
