numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num_escolhido = int(input('Digite um número ente 0 e 20: '))
while num_escolhido not in range(0,20):
    print('Valor inválido.')
    num_escolhido = int(input('Digite um número ente 0 e 20: '))

print(f'Você digitou o número {numeros[num_escolhido].upper()}')
