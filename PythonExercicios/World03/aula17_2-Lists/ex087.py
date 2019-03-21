matriz = list()
soma_total = soma_linha_3 = maior_linha_2 = 0

for x in range(0, 3):
    matriz.append([])
    for y in range(0, 3):
        matriz[x].append(int(input(f'Digite o número da célula [{x + 1},{y + 1}]: ')))

for x in range(0, 3):
    for y in matriz[x]:
        soma_total += y
        if x == 1:
            maior_linha_2 = (y if (maior_linha_2 == 0 or y > maior_linha_2) else maior_linha_2)
        elif x == 2:
            soma_linha_3 += y

        print(f'[ {y} ]', end='')
    else:
        print()
else:
    print(f'A soma de todos os termos da matriz é {soma_total}')
    print(f'A soma de todos os termos da terceira coluna é {soma_linha_3}')
    print(f'O maior número digitado na linha 2 foi {maior_linha_2}')
