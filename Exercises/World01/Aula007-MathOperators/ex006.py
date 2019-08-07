from math import sqrt

n1 = float(input('Digite um número\n'))
print('O dobre de {0} é {1}.\nO trípulo de {0} é {2}.\nA raiz quadrada de {0} é {3}.'.format(n1, (n1*2), (n1*3), (n1**(1/2))))
print('A raiz (function) quadrada de {0} é {1}.'.format(n1, sqrt(n1)))
