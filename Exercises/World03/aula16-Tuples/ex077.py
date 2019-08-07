lista_palavras = ('calangao',
                  'python',
                  'puma',
                  'relogio',
                  'louça',
                  'jantar',
                  'amor',
                  'sexo',
                  'aur')

for palavra in lista_palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print('\nFIM!')
