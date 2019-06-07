import moeda


price = float(input('Digite um preço: '))
print(f'O dobro de {moeda.moeda(price)} é {moeda.moeda(moeda.dobro(price))}')
print(f'A metade de {moeda.moeda(price)} é {moeda.moeda(moeda.metade(price))}')
print(f'O preço acréscimo de 10% é {moeda.moeda(moeda.aumentar(price, 10))}')
print(f'O preço com desconto de 20% é {moeda.moeda(moeda.diminuir(price, 20))}')
