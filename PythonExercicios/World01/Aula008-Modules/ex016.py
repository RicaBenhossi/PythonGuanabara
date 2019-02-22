from math import floor, trunc

num = float(input('Digite um número:\n'))
print('A porção interia do número digitado é: {}'.format(floor(num)))
print('A porção interia do número digitado é: {}'.format(trunc(num)))
# without importing an external module
print('A Porção inteira do número digitado é: {}'.format(int(num)))
