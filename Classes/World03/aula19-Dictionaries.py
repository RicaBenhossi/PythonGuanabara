# To start a dictionay just name = {} or name = dict()
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas.items())
print(pessoas.keys())
print(pessoas.values())
# print(pessoas[0]) # ERROR no index 0
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]}.')

print(pessoas.values())

for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)

for k, v in pessoas.items():
    print(f'{k} is {v}.')

# Add new items: just add as a regurlar variable.
pessoas['altura'] = 1.83
print(pessoas.items())
# Remove itens
del pessoas['sexo']
print(pessoas.items())
# Change an item
pessoas['nome'] = 'Leandro'
print(pessoas.items())

print()
print('=' * 80)
print()

estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil = list()
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[1]['uf'])
print(brasil[0]['sigla'])

print()
print('=' * 80)
print()

print('Here will be dragons! Dictionaries do not allow slicing. To copy a dict you neewd to use function COPY()')

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    # Copying like this will subscribe all items in list
    # brasil.append(estado)
    # Copying like this will return an error. Dicts doesn't allow slicing
    # brasil.append(estado[:])
    # Thisis the right way to copy a Dict
    brasil.append(estado.copy())
print()
for e in brasil:
    for k, v in e.items():
        print(f'A {k} é {v}.')
    print('-' * 40)

print('=' * 40)

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
