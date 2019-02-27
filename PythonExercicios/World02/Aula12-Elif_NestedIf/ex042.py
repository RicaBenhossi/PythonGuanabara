reta1 = float(input('Informe o comprimento da reta 1 '))
reta2 = float(input('Informe o comprimento da reta 2 '))
reta3 = float(input('Informe o comprimenro da reta 3 '))
if ((reta1 < (reta2 + reta3)) and (reta2 < (reta1 + reta3)) and (reta3 < (reta1 + reta2))):
    # MY WAY....
    # if ((reta1 != reta2) and (reta1 != reta3) and (reta2 != reta3)):
    #     print('Essas retas formam um triângulo ESCALENO!')
    # elif ((reta1 == reta2) and (reta1 == reta3) and (reta2 == reta3)):
    #     print('Essas retas forma um triângulo EQUILÁTERO!')
    # else:
    #     print('Essas retas forma um triângulo ISÓCELES!')

    # TEACHERS WAY (BETTER) Python accepts this.
    if ((reta1 != reta2 != reta3 != reta1)):
        print('Essas retas formam um triângulo ESCALENO!')
    elif ((reta1 == reta2 == reta3)):
        print('Essas retas forma um triângulo EQUILÁTERO!')
    else:
        print('Essas retas forma um triângulo ISÓCELES!')
else:
    print('Os segmentos de reta não podem forma um triângulo.')
