# NOTE: This methond was transfered to MODULOS.PY. So, to use them, import the module.
# def fatorial(n):
#     f = 1
#     for c in range(1, n+1):
#         f *= c
#     return f


# def dobro(n):
#     return n * 2


# def triplo(n):
#     return n * 3

import Modulos as uteis

num = int(input('Type a value: '))
# With the methods in the same file
# fat = fatorial(num)
# print(f'The fatorial of {num} is {fat}')
# print(f'The double of {num} is {dobro(num)}')

# With methos imported from MODULOS.PY
fat = uteis.fatorial(num)
print(f'The fatorial of {num} is {fat}')
print(f'The double of {num} is {uteis.dobro(num)}')

