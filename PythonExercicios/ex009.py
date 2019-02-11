numero = int(input('Digite um número\n'))
print('A tabuada de {0} é:\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}\n{9}\n{10}'.format(numero, (numero*1),(numero*2),(numero*3),(numero*4),(numero*5),(numero*6),(numero*7),(numero*8),(numero*9),(numero*10)))
print('\nA tabuada do {} (com FOR) é:'.format(numero))
for x in (range(1,10)):
    print(numero * x)