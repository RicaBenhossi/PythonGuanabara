valores = list()
maior = menor = 0

for pos in range(0, 5):
    valores.append(int(input(f'Digite o {pos + 1} número: ')))
    if pos > 0:
        if maior < valores[pos]:
            maior = valores[pos]
        elif menor > valores[pos]:
            menor = valores[pos]
    else:
        maior = menor = valores[pos]

print('-' * 20)
print(f'O maior número foi {maior}, digitado na(s) posição(ões) ', end='')
for posicao, valor in enumerate(valores):
    if valor == maior:
        print(f'{posicao}... ', end='')
print()
print(f'O menor número foi {menor}, digitado na(s) posição(ões) ', end='')
for posicao, valor in enumerate(valores):
    if valor == menor:
        print(f'{posicao}... ', end='')
print()
