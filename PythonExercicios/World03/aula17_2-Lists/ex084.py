pessoas = list()
pesadas = list()
leves = list()

while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))

    if pessoas[1] >= 85:
        pesadas.append(pessoas[:])
    else:
        leves.append(pessoas[:])

    pessoas.clear()
    while True:
        resposta = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
        if resposta not in 'SN':
            print('Opção inválida.')
        else:
            break

    if resposta == 'N':
        break

print('-' * 50)
print(f'Foram digitadas ao todo {len(pesadas) + len(leves)} pessoa(s)')
if pesadas:
    print(f'A(s) pessoa(s) com peso maior que 85 KG foi(ram): ', end='')
    for nome in pesadas:
        print(f'{nome[0]} ', end=' ')

    print()
else:
    print('Não foi informada nenhuma pessoa com peso acima de 85 Kg.')

if leves:
    print(f'A(s) pessoa(s) com peso menor que de 85 KG foi(ram): ', end='')
    for nome in leves:
        print(f'{nome[0]}', end=' ')

    print()
else:
    print('Não foi informada nenhuma pessoa com peso abaixo de 85 KG.')

