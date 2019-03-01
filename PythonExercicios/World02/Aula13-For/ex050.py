soma_no_if = 0
soma = 0
for x in range(1, 7):
    num = int(input('Digite o {} número: '.format(x)))
    # We can do it with a regular if
    if (x % 2 == 0):
        soma_no_if += x
    # We can do with an if in a unique line
    soma = soma + (x if x % 2 == 0 else 0)
print('A soma no if convencional é {}.'.format(soma_no_if))
print('A soma no if em uma linha é {}.'.format(soma))
