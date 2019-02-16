dias = int(input('Quantos dias o carro ficou alugado?\n'))
kilometros = float(input('quantos kilometros foram percorridos?\n'))
valorKm = kilometros * 0.15
diaria = dias * 60
print('\n{:=^40}\n'.format(' Subtotal '))
print('Kilometragem percorrida: {0}km\nValor por km rodado: R$0,15\nValor Total da Kilometragem: R${1}\n\n{2}\n'
      .format(kilometros, valorKm, ('-' * 20)))
print('Dias de Aluguél: {0}\nValor da diária: R$60,00\nValor Total de Diárias: R${1}\n\n{2}\n'
      .format(dias, diaria, ('-' * 20)))
print('=' * 40)
print('O Valor total a ser pago é de R${:.2f}'.format(valorKm + diaria))
