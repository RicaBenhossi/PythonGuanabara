import coin


# price = float(input('Digite um preço: '))
price = 100
print(f'O dobro de {coin.format_coin(price)} é {coin.dobro(price, True)}')
print(f'A metade de {coin.format_coin(price)} é {coin.metade(price, True)}')
print(f'O preço acréscimo de 10% é {coin.aumentar(price, 10, True)}')
print(f'O preço com desconto de 20% é {coin.diminuir(price, 20, True)}')

print(coin.resumo(price, 20, 10))
