val_produto = float(input('Informe o valor do produto: R$'))
cod_forma_pagamento = int(input('Qual a forma de Pagamento?\n\
    \t[ 1 ] À VISTA (DINHEIRO/CHEQUE)\n\
    \t[ 2 ] À VISTA (CARTÃO DE CRÉDITO)\n\
    \t[ 3 ] PARCELADO (CARTÃO DE CRÉDITO)\n\n\
    Forma Escolhida: '))
if (cod_forma_pagamento == 1):
    val_total = val_produto - (val_produto * 0.1)
elif (cod_forma_pagamento == 2):
    val_total = val_produto - (val_produto * 0.05)
elif (cod_forma_pagamento == 3):
    qtd_parcelas = int(input('Em quantas parcelas você deseja? '))
    if (qtd_parcelas <= 2):
        val_total = val_produto
    else:
        val_total = val_produto + (val_produto * 0.2)
    val_parcela = val_total / qtd_parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} {} JUROS.'.format(qtd_parcelas, val_parcela, ('COM' if qtd_parcelas > 2 else 'SEM')))
else:
    print('Forma de pagamento inválida!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(val_produto, val_total))
