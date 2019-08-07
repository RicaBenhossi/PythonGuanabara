primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão dessa PA: '))
# Math concept od AP
decimo = (primeiro_termo + (10 - 1) * razao) + razao
for x in range(primeiro_termo, decimo, razao):
    print(x, end=', ')
print('ACABOU')
