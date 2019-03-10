total = menor_preco = 0.0
qtd_produto_mais_mil = 0
nome_prod_mais_barato = ''
while True:
    nome_produto = str(input('Informe o nome do produto: ')).upper().strip()
    preco = float(input('Informe o preço do produto: R$'))
    total += preco
    if (preco < menor_preco) or (menor_preco == 0):
        menor_preco = preco
        nome_prod_mais_barato = nome_produto

    if preco >= 1000:
        qtd_produto_mais_mil += 1
    while True:
        continua = str(input('Deseja informar mais produtos? [S/N] ')).upper().strip()[0]
        if continua not in 'NS':
            print('Opção inválida.')
        else:
            break
    if continua == 'N':
        break
print(f'O total gastro foi de R${total}')
print(f'O produto mais barato registrado foi o(a) {nome_prod_mais_barato}')
print(f'Foram registrados {qtd_produto_mais_mil} produto(s) que custa(m) mais de R$1000,00')
