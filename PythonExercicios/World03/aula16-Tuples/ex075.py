numeros = (int(input('Digite um número: ')), 
           int(input('Digite outro número: ')), 
           int(input('Digite mais um número: ')), 
           int(input('Digite o último número: ')))
print(f'Você digitou os valores {numeros}')
print(f'O número nove (9) apareceu {numeros.count(9)} vez(es).')
if 3 in numeros:
    print(f'O número três (3) apareceu na posição {numeros.index(3)}.')
else:
    print('O número 3 não foi digitado.')
print('Os números pares digitados foram: ', end='')
for x in numeros:
    if x % 2 == 0:
        print(x, end=' ')