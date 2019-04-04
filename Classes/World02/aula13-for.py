for c in range(1, 6):
    print('oi')
print('fim\n')

for c in range(0, 5):
    print(c)
print('fim\n')
# Range params (start, stop, step)
for c in range(6, 0, -1):
    print(c)
print('fim\n')

for c in range(0, 10, 2):
    print(c)
print('fim\n')

inicial = int(input('Digite um valor inicial: '))
final = int(input('Digite um valor final: '))
for x in range(inicial, final):
    print(x)
print('Fim\n')

s = 0
for x in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores é {}.'.format(s))
