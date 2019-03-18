numeros = list()

while True:
    num = int(input('Digite um número: '))
    if num not in numeros:
        numeros.append(num)
        print('Adicionado com sucesso.')
    else:
        print('Número já consta na lista.')

    while True:
        continua = str(input('Deseja Continuar? [S/N]')).upper().strip()[0]
        if continua not in 'SN':
            print('Opção inválida.')
        else:
            break

    if continua == 'N':
        numeros.sort()
        break
print(f'Os números digitados foram {numeros}.')
