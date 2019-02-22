num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))
maior = num1
menor = num2
if (maior < menor):
    maior = num2
    menor = num1

if (maior < num3):
    maior = num3
else:
    if (menor > num3):
        menor = num3
print('O maior número é {} e o menor número é {}.'.format(maior, menor))
