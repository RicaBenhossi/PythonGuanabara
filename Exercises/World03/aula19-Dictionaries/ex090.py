aluno = dict()
turma = list()
while True:
    aluno['aluno'] = str(input('Informe o nome do Aluno: '))
    aluno['média'] = float(input('Digite a média do aluno: '))
    # aluno['status'] = ('APROVADO' if aluno['media'] >= 7 else 'REPROVADO')
    if aluno['média'] >= 7:
        aluno['status'] = 'APROVADO'
    elif aluno['média'] >= 5:
        aluno['status'] = 'RECUPERAÇÃO'
    else:
        aluno['status'] = 'REPROVADO'
    turma.append(aluno.copy())
    aluno.clear()

    while True:
        continua = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
        if continua not in 'SN':
            print('Opção inválida.')
        else:
            break

    if continua == 'N':
        break

print(f'{"ALUNO":^20}{"MÉDIA":^5}{"STATUS":^15}')
print('-' * 40)
for a in turma:
    print(f'{a["aluno"].upper():<20}{a["média"]:^5}{a["status"]:^15}')
