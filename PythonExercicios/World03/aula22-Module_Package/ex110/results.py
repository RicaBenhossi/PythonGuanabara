import moeda


price = float(input('Digite um preço: '))
print(f'O dobro de {moeda.moeda(price)} é {moeda.dobro(price, True)}')
print(f'A metade de {moeda.moeda(price)} é {moeda.metade(price, True)}')
print(f'O preço acréscimo de 10% é {moeda.aumentar(price, 10, True)}')
print(f'O preço com desconto de 20% é {moeda.diminuir(price, 20, True)}')
moeda.resumo(price, 20, 10)
