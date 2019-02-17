# My way using IF
# numero = str(input('Digite um número entre 0 e 9999\n'))
# print('unidade: {}'.format(numero[len(numero) - 1]))
# if (len(numero) > 1):
#     print('dezena: {}'.format(numero[len(numero) - 2]))
#     if (len(numero) > 2):
#         print('centena: {}'.format(numero[len(numero) - 3]))
#         if (len(numero) > 3):
#             print('milhar: {}'.format(numero[len(numero) - 4]))

# Teachers' way
num = int(input('Informe um número\n'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}:'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
