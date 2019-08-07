maiordeidade = qtd_homens = mulheresmenos20 = 0

while True:
    idade = int(input('Informe a idade da pessoa: '))
    while True:
        sexo = str(input('Informe os sexo da pessoa [F/M]: ')).upper().strip()[0]
        if sexo not in 'FM':
            print('Sexo informado é inválido.')
        else:
            break

    if idade >= 18:
        maiordeidade += 1

    if sexo == 'M':
        qtd_homens += 1
    elif idade <= 20:
        mulheresmenos20 += 1

    while True:
        continua = str(input('Deseja Continuar? [S/N]')).upper().strip()[0]
        if continua not in 'SN':
            print('Opção inválida.')
        else:
            break

    if continua == 'N':
        break

print(f'Foram informadas {maiordeidade} pessoas maior(es) de idade.')
print(f'Foram informado {qtd_homens} homens.')
print(f'Foram informadas {mulheresmenos20} mulheres com menos de 20 anos.')
