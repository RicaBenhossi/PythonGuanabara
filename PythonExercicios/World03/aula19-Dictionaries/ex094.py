grupo = list()
pessoa = dict()
media_idade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input(f'Digite o nome da {len(grupo) + 1} pessoa: '))
    pessoa['idade'] = int(input('Digite a idade: '))
    media_idade += pessoa['idade']
    while True:
        sexo = str(input('Digite o sexo [F = Feminino / M = Masculino / O = Outro]: ')).strip().upper()
        if not sexo or sexo[0] not in 'FMO':
            print('Opção inválida')
        else:
            break
    pessoa['sexo'] = sexo
    # NOTE When doing like below, it makes a link between 2 variables. USE COPY. SAFER.
    # grupo.append(pessoa)
    grupo.append(pessoa.copy())

    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if not continuar or continuar[0] not in 'SN':
            print('Opção inválida!')
        else:
            break

    if continuar != 'S':
        break

media_idade = round((media_idade / len(grupo)), 0)

print(grupo)
print('-' * 50)
print('\tItem A')
print(f'Foi(ram) cadastrada(s) ao todo {len(grupo)} pessoa(s).')
print('-' * 50)
print('\tItem B')
print(f'A idade média do grupo é {media_idade:5.2f}.')
print('-' * 50)
print('\tItem C e D')
mulher = list()
pessoa_idade_maior_media = list()
for pessoa in grupo:
    if pessoa['sexo'] == 'F':
        mulher.append(pessoa["nome"])
    if pessoa['idade'] > media_idade:
        # idade_maior_media = dict()
        # idade_maior_media['nome'] = pessoa['nome'].upper()

        # idade_maior_media['idade'] = pessoa['idade']
        pessoa_idade_maior_media.append(pessoa)

# ITEM C
print('A(s) mulher(es) da lista é(são):')
for pessoa in mulher:
    print(f'\t{pessoa.upper()}')
# ITEM D
print('-' * 50)
print(f'A(s) pessoa(s) com idade acima da média {media_idade} é(são)')
if pessoa_idade_maior_media:
    for pessoa in pessoa_idade_maior_media:
        for pessoa_keys, pessoa_value in pessoa.items():
            print(f'\t{pessoa_keys} = {pessoa_value}', end='; ')
        print()
else:
    print('Nenhuma')

print('PROGRAMA ENCERRADO')
