from random import choice
aluno1 = input('Digite o nome do aluno 1\n')
aluno2 = input('Digite o nome do aluno 2\n')
aluno3 = input('Digite o nome do aluno 3\n')
aluno4 = input('Digite o nome do aluno 4\n')
lista_alunos = [aluno1, aluno2, aluno3, aluno4]
print('O aluno sorteado foi: {}'.format(choice(lista_alunos)))
