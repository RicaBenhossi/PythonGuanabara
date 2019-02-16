from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo\n'))
print('O seno do ângulo {0} é: {1:.2f}\nO coseno do ângulo {0} é: {2:.2f}\nA tangente do ângulo {0} é: {3:.2f}'
      .format(angulo, sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))
