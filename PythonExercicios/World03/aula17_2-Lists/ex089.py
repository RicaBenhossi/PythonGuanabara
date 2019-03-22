alunos = list()

while True:
    alunos.append(list())
    for x in range(0, len(alunos)):
        alunos[x].append(str(input('Nome do aluno: ')))
        notas = list()
        media = 0
        for y in range(0, 2):
            notas.append(float(input(f'Nota {y + 1}: ')))
            media += notas[y]
        else:
            alunos[x].append(notas)
            alunos[x].append(media / 2)

    while True:
        continuar = str(input('Deseja continuar?[S/N]')).upper().strip()[0]
        if continuar not in 'NS':
            print('Opção inválida.')
        else:
            break
    if continuar == 'N':
        break

while True:
    break

