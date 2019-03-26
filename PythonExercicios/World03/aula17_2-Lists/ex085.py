lista = list(([], []))

for x in range(0, 7):
    valor = int(input(f'Digite o {x}o. valor: '))
    if (valor % 2 == 0) or (valor == 0):
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram {lista[0]}.')
print(f'Os valores ímpares digitados foram {lista[1]}.')
