frase = str(input('Escreva uma frase: ')).strip().upper()
frase_sem_espacos = ''.join(frase.split(' '))
frase_espelho = str('')
for x in range(len(frase_sem_espacos) - 1, -1, -1):
    frase_espelho += frase_sem_espacos[x]
print('A frase espelho é {}.'.format(frase_espelho))
print('A frase {} {}É um PALÍNDROMO!'.format(frase, 'NÃO ' if frase_sem_espacos != frase_espelho else ''))

# You can also use slicing to solve
frase = str(input('Escreva uma frase: ')).strip().upper()
frase_sem_espacos = ''.join(frase.split(' '))
frase_espelho = frase_sem_espacos[::-1]
print('A frase espelho é {}.'.format(frase_espelho))
print('A frase {} {}É um PALÍNDROMO!'.format(frase, 'NÃO ' if frase_sem_espacos != frase_espelho else ''))
