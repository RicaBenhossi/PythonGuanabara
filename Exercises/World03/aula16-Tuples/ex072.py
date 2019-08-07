numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num_escolhido = int(input('Digite um número entre 0 e 20: '))
    if num_escolhido in range(0, 20):
        break
    print('Valor inválido.')

print(f'Você digitou o número {numeros[num_escolhido].upper()}')
