# import math
import random
# This bellow must be installed via pip3 (pip3 install emoji)
import emoji
from math import sqrt, floor
num = int(input('digite um número: '))
# This commands commented bellow is user when you import ALL math library.
# raiz = math.sqrt(num)
# print('A raiz é {}'.format(math.floor(raiz)))
raiz = sqrt(num)
print('A raiz é {}'.format(floor(raiz)))
# A Random number between 0 and 1
print('Número aleatório: {}'.format(random.random()))
# A Random integer number between 1 and 100 (you can choose)
print('Número aleatório: {}'.format(random.randint(1, 100)))
print(emoji.emojize('OLAR :sunglasses:', use_aliases=True))
