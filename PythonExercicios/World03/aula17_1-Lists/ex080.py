listagem = list()

for x in range(0, 5):
    num = int(input(f'Digite o {x + 1} número: '))
    if x == 0 or num > listagem[-1]:  # Listagem[-1] is the last item.
        listagem.append(num)
    else:
        for posicao, valor in enumerate(listagem):
            if num < valor:
                listagem.insert(posicao, num)
                break

print(f'Os valores digitados foram {listagem}')
