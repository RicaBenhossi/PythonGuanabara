nome = str(input('Qual o seu nome?' ))
if (nome == 'Natalia'):
    print('Que nme lindo !!!!')
elif (nome == 'Pedro' or nome == 'João' or nome == 'Maria'):
    print('Seu nome é bem comum no Brasil.')
elif (nome in 'Ana Cláudia Jéssica Juliana'):
    print('Nome femino.')
else:
    print('Seu nome é bem normal...')
print('tenha um bom dia {}.'.format(nome))
