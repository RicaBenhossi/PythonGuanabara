

# NOTE Exercise 107 - Create functions (aumentar, diminuir, metade e dobro).
# NOTE Exercise 109 - Criado parâmetro opcional (default FALSE) nas funções do exercício 107.
def aumentar(num, porcentagem, formatado=False):
    if formatado:
        return format_coin(num + (num * (porcentagem / 100)))
    else:
        return num + (num * (porcentagem / 100))


def diminuir(num, porcentagem, formatado=False):
    if formatado:
        return format_coin(num - (num * (porcentagem / 100)))
    else:
        return num - (num * (porcentagem / 100))


def dobro(num, formatado=False):
    if formatado:
        return format_coin(num * 2)
    else:
        num * 2


def metade(num, formatado=False):
    if formatado:
        return format_coin(num / 2)
    else:
        return num / 2


# NOTE Exercise 108
def format_coin(num):
    return f'R${num:.2f}'.replace('.', ',')
