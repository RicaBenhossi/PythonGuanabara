pessoas = list()
pesadas = list()
leves = list()

while True:
    pessoas.append([str(input('Nome: ')), float(input('Peso: '))])

    while True:
        resposta = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
        if resposta not in 'SN':
            print('Opção inválida.')
        else:
            break

    if resposta == 'N':
        break
print(pessoas)

mais_pesadas = max(pessoas)[1]
mais_leves = min(pessoas)[1]

for nome, peso in pessoas:
    if peso == mais_pesadas:
        pesadas.append(nome)
    elif peso == mais_leves:
        leves.append(nome)

print(f'Você informou ao todo {len(pessoas)} pessoa(s)')
print(f'O maior peso digitado foi {mais_pesadas} Kg, das pessas {pesadas}.')
print(f'O meno peso digitado foi {mais_leves} Kg, das pessoas {leves}.')
