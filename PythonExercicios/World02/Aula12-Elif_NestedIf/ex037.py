num = int(input('Digite o número para conversão: '))
cod_conversao = int(input('Informe o código da conversão desejada:\
    \n\t1 - BINÁRIO\
    \n\t2 - OCTAL\
    \n\t3 - HEXADECIMAL\n'))
if (cod_conversao == 1):
    print('O número {} em binário é {}.'.format(num, bin(num)))
elif (cod_conversao == 2):
    print('O número {} em Octal é {}.'.format(num, oct(num)))
elif (cod_conversao == 3):
    print('O numero {} em Hexadecimal é {}.'.format(num, hex(num)))
else:
    print('Codigo de conversão inválido.')
# To not show the indicative of binary/octal/hexadecimal, use SLICING
if (cod_conversao == 1):
    print('O número {} em binário é {}.'.format(num, bin(num)[2:]))
elif (cod_conversao == 2):
    print('O número {} em Octal é {}.'.format(num, oct(num)[2:]))
elif (cod_conversao == 3):
    print('O numero {} em Hexadecimal é {}.'.format(num, hex(num)[2:]))
else:
    print('Codigo de conversão inválido.')

