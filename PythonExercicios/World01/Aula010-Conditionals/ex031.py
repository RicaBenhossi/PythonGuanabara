distancia = float(input('Qual a distância da sua viagem? '))
if (distancia <= 200):
    print('A passagem custará R${:.2f}'.format(distancia * 0.5))
else:
    print('A passagem custará R${:.2f}'.format(distancia * 0.45))
