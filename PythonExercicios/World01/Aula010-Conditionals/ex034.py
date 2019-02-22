salario = float(input('Informe o salário: '))
if (salario > 1250):
    print('O seu novo salário com reajuste de 10% é de R${:.2f}.'.format(salario + (salario * 0.1)))
else:
    print('O seu nove salário com reajuste de 15% é de R${:.2f}.'.format(salario + (salario * 0.15)))
