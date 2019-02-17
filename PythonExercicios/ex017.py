from math import hypot
cateto_adjascente = float(input('Digite a medida do cateto adjascente\n'))
cateto_oposto = float(input('Digite a medida do cateto oposto\n'))
print('A medida da hipotenusa é: {:.2f}'.format(hypot(cateto_adjascente, cateto_oposto)))

