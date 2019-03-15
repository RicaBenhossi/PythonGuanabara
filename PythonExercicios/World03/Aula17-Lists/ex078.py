valores = list()
maior = menor = pos_maior = pos_menor = 0

for x in range(0, 5):
    valores.append(int(input(f'Digite o {x + 1} número: ')))

for pos in range(0, len(valores)):
    if pos > 0:
        if maior < valores[pos]:
            maior = valores[pos]
            pos_maior = pos
        elif menor > valores[pos]:
            menor = valores[pos]
            pos_menor = pos
    else:
        maior = valores[pos]
        pos_maior = pos
        menor = maior
        pos_meno = pos_maior
print('-' * 20)
print(f'O maior número foi {maior}, digitado na posição {pos_maior}.')
print(f'O menor número foi {menor}, digitado na posição {pos_menor}.')
