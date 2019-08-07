def escreva(mensagem):
    print('~' * (len(mensagem) + 2))
    print(f' {mensagem:^2} ')
    print('~' * (len(mensagem) + 2))


texto = str(input('Digite o texto que deseja formatar: ')).strip()
escreva(texto)
