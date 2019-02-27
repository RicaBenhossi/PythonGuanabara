nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('Sua média é {}.'.format(media))
if (media < 5):
    print('REPROVADO!')
elif (media < 7):
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')
