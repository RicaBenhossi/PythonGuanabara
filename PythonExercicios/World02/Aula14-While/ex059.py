num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
print('Qual operação deseja realizar?\n\
\t[ 1 ] SOMAR\n\
\t[ 2 ] Multiplicar\n\
\t[ 3 ] Maior\n\
\t[ 4 ] Novos números\n\
\t[ 5 ] Sair do programa')
opcao = int(input('Digite a opção desejada: '))
while opcao != 5:
    if opcao == 1:
        print('A soma entre {} e {} é {}.'.format(num1, num2, num1 + num2))
    elif opcao == 2:
        print('A multiplicação entre {} e {} é {}.'.format(num1, num2, num1 * num2))
    elif opcao == 3:
        if num1 > num2:
            print('{} é maior que {}.'.format(num1, num2))
        elif num1 < num2:
            print('{} é maior que {}.'.format(num2, num1))
        else:
            print('Os números são iguais...')
    elif opcao == 4:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
    else:
        print('Opção inválida!')
    opcao = int(input('Digite a opção desejada: '))
print('Programa Finalizado!')
