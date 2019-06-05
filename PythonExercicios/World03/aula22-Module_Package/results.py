import coin


price = float(input('Digite um preço: '))
print(f'O dobro de {coin.format_coin(price)} é {coin.dobro(price)}')
print(f'A metade de {coin.format_coin(price)} é {coin.metade(price)}')
print(f'O preço acréscimo de 10% é {coin.aumentar(price, 10)}')
print(f'O preço com desconto de 20% é {coin.diminuir(price, 20)}')
