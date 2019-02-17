nome_completo = str(input('Digite o seu nome\n').strip())
nome_separado = nome_completo.split()
print('O primeiro nome é {} e o sobrenome é {}'.format(nome_separado[0], nome_separado[len(nome_separado) - 1]))
