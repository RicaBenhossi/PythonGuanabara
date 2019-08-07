teste = int(input())
primeiro_termo = int(input('Digite o primeiro temro da PA: '))
razao = int(input('Digite a razão da PA: '))
termos = 10
p = num = 0
while p < termos:
    p += 1
    num += razao
    print('{}'.format(num), end=' -> ')
    if p == termos:
        print('PAUSA')
        termos += int(input('Deseja imprimir mais quantos termos? '))
print('Acabou!')
