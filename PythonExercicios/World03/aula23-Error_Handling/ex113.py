def LeiaInt(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except ValueError:
            print('Valor inválido.')
        except KeyboardInterrupt:
            print('Operação LeiaInt encerrada pelo Operador.')
            exit
        else:
            return numero
            break

def LeiaFloat(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
        except ValueError:
            print('Valor inválido.')
        except KeyboardInterrupt:
            print('Operação LeiaFloat encerrada pelo Operador.')
            break
        else:
            return numero
            break


n = LeiaInt('Digite um número inteiro: ')
m = LeiaFloat('Digite um número Decimal: ')
print(n)
print(m)
