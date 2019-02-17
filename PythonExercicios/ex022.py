nome = str(input('Digite o seu nome\n').strip())
print(nome.upper())
print(nome.lower())
print(nome.capitalize())
print(nome.title())
# My way
print('O nome possui ao todo {} caracteres.'.format(len(nome.replace(' ', ''))))
# Teachers' way
print('O nome possui ao todo {} caracteres.'.format(len(nome) - nome.count(' ')))
# My way
nome_separado = nome.split()
print('O primeiro nome possui ao todo {} caracteres.'.format(len(nome_separado[0])))
# Teachers' way
print('O primeiro nome possui ao todo {} caracteres '.format(nome.find(' ')))
