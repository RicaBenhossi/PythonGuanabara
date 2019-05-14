def LeiaInt(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            break
        except ValueError:
            print('Valor inválido.')
    return numero


n = LeiaInt('Digite um número inteiro: ')
print(n)
