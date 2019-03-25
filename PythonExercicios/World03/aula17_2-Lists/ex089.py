turma = list()
# turma = list((['ana', [10.0, 8.9], 9.45], ['pedro', [3.0, 6.0], 4.5], ['natalia', [10.0, 10.0], 10.0], ['jose', [2.6, 5.6], 4.1], ['marcos', [7.5, 8.7], 8.1], ['lara', [7.8, 9.7], 8.75]))
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

print(f'{"No.":<5}{"NOME":<30}{"MÉDIA":<4}\n{"-" * 40}')

for pos, aluno in enumerate(turma):
    print(f'{pos:<5}{aluno[0]:<30}{aluno[2]:<4}')

while True:
    print('-' * 40)
    mostrar_aluno = input('Desja mostrar as notas de qual aluno?\n[S - Sair] ')
    if (mostrar_aluno.isalpha()) and (mostrar_aluno.upper().strip()[0] == 'S'):
        break
    elif (mostrar_aluno.isnumeric()) and (int(mostrar_aluno) < len(turma)):
        print(f'As notas do(a) aluno(a) {turma[int(mostrar_aluno)][0].upper()} são: {turma[int(mostrar_aluno)][1]}')
    else:
        print('Opção inválida.')
print(f'{"<<< VOLTE SEMPRE >>>":^50}')
