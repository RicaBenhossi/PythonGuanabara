media = dict()
while True:
    media['aluno'] = str(input('Informe o nome do Aluno: '))
    media['media'] = float(input('Digite a média do aluno: '))
    media['status'] = ('APROVADO' if media['media'] >= 7 else 'REPROVADO')

    while True:
        continua = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
        if continua not in 'SN':
            print('Opção inválida.')
        else:
            break

    if continua == 'N':
        break

print(f'{"ALUNO":^20}{"MÉDIA":^5}{"STATUS":^10}')
for v in media.values():
    for k in media.keys():
        print(f'O(a) aluno(a) {media[k]} posusui media{media} e está {status}(A).')
