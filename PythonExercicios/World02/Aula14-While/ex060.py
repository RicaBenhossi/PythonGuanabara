from math import factorial

fatorial = int(input('Informe o número que deseja saber o fatorial: '))
anterior = resultado = fatorial
while anterior != 1:
    resultado = resultado * (anterior - 1)
    anterior -= 1
print('O resultado (WHILE) é {}.'.format(resultado))

anterior = resultado = fatorial
for x in range(fatorial - 1, 1, -1):
    resultado = resultado * x
print('O resultado (FOR) é {}.'.format(resultado))

print('O resultado (MODULE) é {}.'.format(factorial(fatorial)))
