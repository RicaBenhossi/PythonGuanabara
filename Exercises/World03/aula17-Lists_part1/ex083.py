expressao = str(input('Digite a sua expressão: '))
# if (expressao.count('(') != expressao.count(')')) or (expressao.index('(') > expressao.index(')')):
#     print('Sua expressão é inválida!')
# else:
#     print('Sua expressão é válida!')
pilha = list()

for simbolo in expressao:
    if simbolo == '(':
        pilha.append(simbolo)
    elif simbolo == ')':
        if pilha:
            pilha.pop()
        else:
            pilha.append(')')
            break

if pilha:
    print('Sua expressão é inválida!')
else:
    print('Sua expressão é válida!')
