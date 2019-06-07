def aumentar(preco=0, taxa=0, formato=False):
    return moeda(preco + (preco * (taxa / 100))) if formato else preco + (preco * (taxa / 100))


def diminuir(preco=0, taxa=0, formato=False):
    return moeda(preco - (preco * (taxa / 100))) if formato else preco - (preco * (taxa / 100))


def dobro(preco=0, formato=False):
    return moeda(preco * 2) if formato else preco * 2


def metade(preco=0, formato=False):
    return moeda(preco / 2) if formato else preco / 2


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(num, aumento, desconto):
    print('-' * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-' * 40)
    print(f'Preço Analisado:{moeda(num):.>24}')
    print(f'Dobro do Preço:{dobro(num, True):.>25}')
    print(f'Metade do Preço:{metade(num, True):.>24}')
    print(f'{aumento}% de aumento:{aumentar(num, aumento, True):.>25}')
    print(f'{desconto}% de desconto:{diminuir(num, desconto, True):.>24}')
    print('-' * 40)
