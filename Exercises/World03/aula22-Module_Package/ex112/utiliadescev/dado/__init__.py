def leia_dinheiro():
    while True:
        try:
            preco = input('Digite o preço: ')
            return float(preco)
            break
        except ValueError:
            print(f'\"{preco}\" não é um valor válido.')

