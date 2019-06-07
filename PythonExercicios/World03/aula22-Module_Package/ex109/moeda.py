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
