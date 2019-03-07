primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a Razao dess PA: '))
p = num = 0
while p < 10:
    num += razao
    print(num, end='')
    p += 1
print('Acabou')

# Teacher did this way
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a Razao dess PA: '))
termo = primeiro_termo
cont = 1
while cont <= 10:
    print('{}'.format(termo), end=' -> ')
    termo += razao
    p += 1
print('Acabou')
