from random import randint
computador = randint(0, 10)
player = -1
tentativas = 0
while player != computador:
    player = int(input('Digite o seu palpite: '))
    tentativas += 1
print('PARABÉNS!!! Você precisou de {} tentativas para acertar.'.format(tentativas))
