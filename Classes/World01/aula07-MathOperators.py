nome = input('Qual o seu nome? ')
print('prazer em te conhecer {:20}!'.format(nome))
print('prazer em te conhecer {:>20}!'.format(nome))
print('prazer em te conhecer {:<20}!'.format(nome))
print('prazer em te conhecer {:^20}!'.format(nome))
print('prazer em te conhecer {:=^20}!'.format(nome))
print('prazer em te conhecer {:*^20}!'.format(nome))
print('prazer em te conhecer {:-^20}!'.format(nome))
print('prazer em te conhecer {:-<20}!'.format(nome))
print('prazer em te conhecer {:->20}!'.format(nome))
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
soma = n1 + n2
sub = n1 - n2
multi = n1 * n2
divisao = n1 / n2
divInt = n1 // n2
resto = n1 % n2
expon = n1 ** n2
print('A Soma é {}, a Subtração é {}, o Produto é {}, a Divisão é {}'.format(soma, sub, multi, divisao))
print('A Soma é {}, a Subtração é {}, o Produto é {}, a Divisão é {}'.format(soma, sub, multi, divisao), end='>>>')
print('A Soma é {} \n a Subtração é {}\n o Produto é {}\n a Divisão é {}'.format(soma, sub, multi, divisao))
print('A Soma é {}, a Subtração (convertida em float) é {:f}, o Produto é {}, a Divisão (arredondada em 3 casas) é {:.3f}'.format(soma, sub, multi, divisao))
print('Divisão inteira é {}, o Resto da Divisão é {} e a Potência é {:#^10}'.format(divInt, resto, expon))
