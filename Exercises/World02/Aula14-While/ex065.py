digitados = maior = menor = media = 0
continuar = 'S'
while continuar in 'Ss':
    digitados += 1
    num = (int(input('Digite um valor: ')))
    media += num
    if digitados == 1:
        maior = menor = num
    else:
        if maior < num:
            maior = num
        elif menor > num:
            menor = num
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Valor inválido. Deseja continuar? [S/N]')).upper().strip()[0]
print('A média entre os valores digitados foi {}.'.format((media / digitados)))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))
