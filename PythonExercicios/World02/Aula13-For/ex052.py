num = int(input('Digite um número: '))
qtd_dividido = 0
for x in range(1, num + 1):
    if(num % x == 0):
        print('{} '.format('\33[1;31m'), end='')
        qtd_dividido += 1
    else:
        print('{} '.format('\33[;036m'), end='')
    print('{}{}'.format(x, '\33[m'), end='')
print('\n\33[;32;470mO número {} \33[m\33[;47;40m{}É PRIMO!\33[m'.format(num, 'NÃO ' if qtd_dividido > 2 else ''))
