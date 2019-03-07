termos = int(input('Quantos termos da sequência de FIBONACCI deseja mostrar? '))
n_atual = 1
x = n_ant1 = n_ant2 = 0
while x < termos:
    if x == 1:
        n_atual += 1
    else:
        n_atual = n_ant1 + n_ant2
    print('{}'.format(n_atual), end=' -> ')
    n_ant2 = n_ant1
    n_ant1 = n_atual
    x += 1
print('Finalizado(user)...')

# Teachers' way
n = termos
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end=' -> ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('{}'.format(t3), end=' -> ')
    t1 = t2
    t2 = t3
    cont += 1
print('Finalizado(Teachers)...')
