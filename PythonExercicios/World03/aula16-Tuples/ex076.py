print('-' * 50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-' * 50)
lista_precos = ('Lápis', 3,
                'borracha', 3.99,
                'caderno', 15.9,
                'mochila', 180.8,
                'caneta', 2.89,
                'compasso', 15.90)
for x in range(0, len(lista_precos), 2):
    print(f'{lista_precos[x].title():.<40}R$ {lista_precos[x + 1]:>7.2f}')
