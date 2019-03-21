matriz = list()

for x in range(0, 3):
    matriz.append([])
    for y in range(0, 3):
        matriz[x].append(int(input(f'Digite o número da célula [{x + 1},{y + 1}]: ')))

for x in range(0, 3):
    for y in range(0, 3):
        print(f'[ {matriz[x][y]} ]', end='')
    else:
        print()
