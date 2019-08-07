import moeda


price = float(input('Digite um preço: '))
print(f'O dobro de {price} é {moeda.dobro(price)}')
print(f'A metade de {price} é {moeda.metade(price)}')
print(f'O preço acréscimo de 10% é {moeda.aumentar(price, 10)}')
print(f'O preço com desconto de 20% é {moeda.diminuir(price, 20)}')
