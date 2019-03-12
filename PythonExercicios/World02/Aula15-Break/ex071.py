print('='*50)
print('{:^50}'.format('BANCALANGÃO. Umbanco AUR!!!'))
print('='*50)
print('\nEsse caixa possui notas de R$50,00, R$20,00, R$10,00 e R$1,00\n')
notas_disponiveis = [50, 20, 10, 1]
qtd_notas = 0
while True:
    quantia_saque = int(input('Qual o valor que deseja sacar: R$'))
    print('Você sacou:')
    for notas in notas_disponiveis:
        qtd_notas = quantia_saque // notas
        quantia_saque = quantia_saque % notas
        if qtd_notas > 0:
            print(f'\t{qtd_notas} nota(s) de {notas}')
    # OLD
        # qtd_cinquenta = qtd_vinte = qtd_dez = qtd_um = 0
        # while True:
        #     quantia_saque = int(input('Qual o valor que deseja sacar: R$'))

            # qtd_cinquenta = quantia_saque // 50
            # quantia_saque = quantia_saque % 50

            # qtd_vinte = quantia_saque // 20
            # quantia_saque = quantia_saque % 20

            # qtd_dez = quantia_saque // 10
            # quantia_saque = quantia_saque % 10

            # qtd_um = quantia_saque

            # print('Você sacou:')
            # if qtd_cinquenta > 0:
            #     print(f'\t{qtd_cinquenta} nota(s) de 50')
            # if qtd_vinte > 0:
            #     print(f'\t{qtd_vinte} nota(s) de 20')
            # if qtd_dez > 0:
            #     print(f'\t{qtd_dez} nota(s) de 10')
            # if qtd_um > 0:
            #     print(f'\t{qtd_um} nota(s) de 1')

    while True:
        continua = str(input('Deseja realizar outro saque? [S/N]')).upper().strip()[0]
        if continua not in 'SN':
            print('Opção inválida.')
        else:
            break

    if continua == 'N':
        break

print('Obrigadopor utilizar nossos serviços. Volte sempre.')
