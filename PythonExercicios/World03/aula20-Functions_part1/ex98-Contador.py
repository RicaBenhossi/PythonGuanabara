from time import sleep


def contador(inicio, fim, passo):
    print('-=' * 50)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if passo == 0:
        passo += 1

    if inicio > fim:
        passo *= -1

    for x in range(inicio, fim + 1, passo):
        print(x, end=' ', flush=True)
        # inicio += passo
        sleep(0.5)

    print('FIM!')


contador(1, 10, 1)
contador(10, 1, 2)
print('Sua vez de fazer uma contagem')
contador((int(input('Inicio: '))), (int(input('Fim: '))), (int(input('Passo: '))))
