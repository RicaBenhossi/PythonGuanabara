# import random
from random import shuffle

a1 = str(input('Digite o nome do primeiro aluno\n'))
a2 = str(input('Digite o nome do segundo aluno\n'))
a3 = str(input('Digite o nome do terceiro aluno\n'))
a4 = str(input('Digite o nome do quarto aluno\n'))
lista_alunos = [a1, a2, a3, a4]
# random.shuffle(lista_alunos)
shuffle(lista_alunos)
print('A ordem de apresentação dos alunos será:')
print(lista_alunos)