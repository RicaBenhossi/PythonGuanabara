num = soma = cont = 0
while True:
    num = (int(input('Digite um número: ')))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Foram digitados {cont} números.')
print(f'A soma entre eles é {soma}')
