velocidade = float(input('Informe a velocidade do veículo: '))
if (velocidade > 80):
    print('Você foi multado em R${:.2f}'.format((velocidade - 80) * 7))
