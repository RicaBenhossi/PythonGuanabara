from datetime import date
idade = 0
maior = 0
menor = 0
for x in range(0, 7):
    idade = date.today().year - (int(input('Digite o ano de nascimento da pessoa {}: '.format(x + 1))))
    if (idade >= 18):
        maior += 1
    else:
        menor += 1
print('{} pessoas são MAIORES de idade e {} são MENORES de idade.'.format(maior, menor))
