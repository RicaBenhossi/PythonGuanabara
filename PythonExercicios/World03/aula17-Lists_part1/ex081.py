numeros = list()
while True:
    numeros.append(int(input('Digite um valor: ')))
    while True:
        continua = str(input('Deseja continuar?[S/N]').upper().strip()[0])
        if continua not in 'SN':
            print('Opção inválida.')
        else:
            break

    if continua == 'N':
        break

print(f'Foram digitados {len(numeros)} valore(s)')
numeros.sort(reverse=True)
print(f'A lista em ordem decrescente é {numeros}')
if 5 in numeros:
    print(f'O número 5 foi encontrado na posição {numeros.index(5)}')
else:
    print('O número 5 não foi encontrado.')
