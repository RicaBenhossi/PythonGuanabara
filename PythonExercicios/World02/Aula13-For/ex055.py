peso_maior = 0
peso_menor = 0
for x in range(1, 6):
    peso = float(input('Digite o peso da {} pessoa: '.format(x)))
    if (x == 1):
        peso_maior = peso
        peso_menor = peso
    else:
        if (peso > peso_maior):
            peso_maior = peso
        elif (peso < peso_menor):
            peso_menor = peso
print('O maior peso foi {}kg e o menor peso foi {}kg.'.format(peso_maior, peso_menor))
