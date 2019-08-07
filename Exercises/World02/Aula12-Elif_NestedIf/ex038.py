num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
if (num1 > num2):
    print('O primeiro número ({}) é MAIOR que o egundo número ({}).'.format(num1, num2))
elif (num2 > num1):
    print('O segundo número ({}) é MAIOR que o primeiro número ({}).'.format(num2, num1))
else:
    print('Os valores informados são IGUAIS.')
