altura = float(input('Informe a sua altura: '))
peso = float(input('Informe o seu peso: '))
imc = (peso / (altura ** 2))
print('Seu IMC é igual à {}.'.format(imc))
if (imc < 18.5):
    print('Você está abaixo do peso ideal.')
elif (imc < 25):
    print('Você está no seu peso ideal.')
elif (imc < 30):
    print('Você está com sobrepeso.')
elif (imc < 40):
    print('Você está obeso.')
else:
    print('Você está com obesidade mórbida.')
