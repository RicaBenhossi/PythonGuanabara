from time import sleep


def fatorial(num, show=False):
    """This method calculate the factorial of the number (num) passed as argument.

    Args:
        num (int): number to calculate the factorial.
        show (bool, optional): Control wheter to show the steps of calculation. Defaults to False.
    """

    print(f'Calculando Fatorial de {num}.')
    resultado = num
    for x in range((num - 1), 0, -1):
        if show:
            print(f'{resultado} x {x} = {resultado * x}')

        resultado *= x
        sleep(0.5)
    print(f'\nO Fatorial de {num} é {resultado}.')


print('=' * 40)
print('\nCálculo Fatorial')
numero = int(input('Digite o número que deseja calcular: '))
while True:
    mostrar_processo = str(input('Deseja mostar o processo do cálculo? [S/N]').strip().upper()[0])
    if mostrar_processo in 'SN':
        show_p = bool(mostrar_processo == 'S')
        break
    else:
        print('Dado inválido.')

fatorial(numero, show_p)
print('=' * 40)
