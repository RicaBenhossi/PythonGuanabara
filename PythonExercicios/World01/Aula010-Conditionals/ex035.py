r1 = float(input('Qual o comprimento da reta 1? '))
r2 = float(input('Qual o comprimento da reta 2? '))
r3 = float(input('Qual o comprimento da reta 3? '))
if ((r1 < (r2 + r3)) and (r2 < (r1 + r3)) and (r3 < (r1 + r2))):
    print('Os segmentos de reta {}, {} e {}, FORMAM um triângulo.'.format(r1, r2, r3))
else:
    print('Os Segmentos de reta {}, {} e {}, NÃO FORMAM um trângulo.'.format(r1, r2, r3))
