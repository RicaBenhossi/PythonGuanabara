from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo += 1

    print('-=' * 50)
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
    if inicio > fim:
        fim -= 1
        if passo > 0:
            passo *= -1
    elif inicio < fim:
        fim += 1
        if passo < 0:
            passo *= -1
    else:
        print('Impossível contar. Mesmo início e fim.')


    for x in range(inicio, fim, passo):
        print(x, end=' ', flush=True)
        # inicio += passo
        sleep(0.5)

    print('FIM!')


# contador(1, 10, 1)
# contador(10, 1, 2)
print('Sua vez de fazer uma contagem')
contador((int(input('Inicio: '))), (int(input('Fim: '))), (int(input('Passo: '))))
