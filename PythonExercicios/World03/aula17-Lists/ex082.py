numeros = list()
num_par = list()
num_impar = list()

while True:
    numeros.append(int(input('Digite um número: ')))

    while True:
        continua = str(input('Deseja continuar?[S/N]')).strip().upper()[0]
        if continua not in 'SN':
            print('Opção inválida.')
        else:
            break

    if continua == 'N':
        break

for valor in numeros:
    if valor % 2 == 0:
        num_par.append(valor)
    else:
        num_impar.append(valor)
print('-' * 50)
print(f'Os números digitados foram {numeros}.')
if num_par:
    print(f'Os números pares digitados foram {num_par}.')
else:
    print('Não foram digitados números pares.')

if num_impar:
    print(f'Os números ímpares digitados foram {num_impar}.')
else:
    print('Não foram digitados números ímpares.')
