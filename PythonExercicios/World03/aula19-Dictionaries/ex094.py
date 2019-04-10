grupo = list()
media_idade = 0
while True:
    pessoa = dict()
    pessoa['nome'] = str(input(f'Digite o nome da {len(grupo) + 1} pessoa: '))
    pessoa['idade'] = int(input('Digite a idade: '))
    media_idade += pessoa['idade']
    pessoa['sexo'] = str(input('Digite o sexo [F = Feminino / M = Masculino / O = Outro]: '))  # TODO: Validar input
    grupo.append(pessoa)

    while True:
        continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if continuar not in 'SN':
            print('Opção inválida!')
        else:
            break

    if continuar != 'S':
        break

print(grupo)
print('-' * 50)
print('\tItem A')
print(f'Foi(ram) cadastrada(s) ao todo {len(grupo)} pessoa(s).')
print('-' * 50)
print('\tItem B')
print(f'A idade média do grupo é {(media_idade / len(grupo)):.0f}.')

