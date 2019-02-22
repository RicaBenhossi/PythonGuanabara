from random import randint
from time import sleep
numero = randint(0, 5)
palpite = int(input('Digite o seu palpite entre 0 e 5: '))
print('Processando...')
sleep(2)
print('O número escolhido foi {}'.format(numero))
if (numero == palpite):
    print('Você acertou. PARABÉNS!!!!')
else:
    print('Você errou. Mais sorte na próxima.')
