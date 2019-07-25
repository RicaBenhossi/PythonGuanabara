def LeiaInt(mensagem):
    try:
        while True:
            try:
                numero = int(input(mensagem))
            except ValueError:
                print('ERRO: Digite um número inteito válido.')
            except KeyboardInterrupt:
                print('Operação LeiaInt encerrada pelo Operador.')
                numero = 0
                break
            else:
                break
    finally:
        return numero


def LeiaFloat(mensagem):
    try:
        while True:
            try:
                numero = float(input(mensagem))
            except ValueError:
                print('ERRO: Digite um valor real válido.')
            except KeyboardInterrupt:
                print('Operação LeiaFloat encerrada pelo Operador.')
                numero = 0
                break
            else:
                break
    finally:
        return numero


inteiro = LeiaInt('Digite um número inteiro: ')
decimal = LeiaFloat('Digite um número Decimal: ')
print(f'O número inteiro digitado foi {inteiro} e o número decimal foi {decimal}.')
