val_salario = float(input('Informe o seu salário: R$'))
val_imovel = float(input('Informe o valor do imóvel: R$'))
qtd_anos = int(input('Informe em quantos anos deseja pgar: '))
val_parcelas = (val_imovel / (qtd_anos * 12))
print('O valor das parcelas é de R${:.2f}.'.format(val_parcelas))
if (val_parcelas > (val_salario * 0.3)):
    print('Esse valor de parcela é maior do que 30% da sua renda mensal.\nFinanciamento NEGADO!')
else:
    print('Valor aprovado!')
