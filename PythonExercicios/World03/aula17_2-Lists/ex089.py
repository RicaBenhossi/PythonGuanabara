turma = list()

while True:
    alunos = list()
    alunos.append(str(input('Nome do aluno: ')))
    notas = list()
    media = 0
    for y in range(0, 2):
        notas.append(float(input(f'Nota {y + 1}: ')))
        media += notas[y]
    else:
        alunos.append(notas)
        alunos.append(media / 2)
        turma.append(alunos)

    while True:
        continuar = str(input('Deseja continuar?[S/N]')).upper().strip()[0]
        if continuar not in 'NS':
            print('Opção inválida.')
        else:
            break
    if continuar == 'N':
        print('=-' * 50)
        break

print(f'{"ID":<5}{"NOME":<30}{"MÉDIA":<4}\n{"-" * 40}')

for pos, nome in enumerate(turma):
    print(f'{pos:<5}{nome:<30}{turma[pos][2]:<4}')

print('-' * 40)
while True:
    mostrar_aluno = input('Desja mostrar as notas de qual aluno?[S - Sair] ')
    if (mostrar_aluno.upper().strip()[0] != 'S') and (not mostrar_aluno.isnumeric()):
        print('Opção inválida.')
    elif mostrar_aluno.upper().strip()[0] == 'S':
        print(f'{"Finalizado":^40}')
        break
    else:
        mostrar_aluno = int(mostrar_aluno)


