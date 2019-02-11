largura = float(input('Digite a largura da parede\n'))
altura = float(input('Digite a altura da parede\n'))
area = largura * altura
qtd_tinta = area / 2
print('A parede possui {} m². Serão necessários {} litros de tinta para pintá-la.'.format(area, qtd_tinta))