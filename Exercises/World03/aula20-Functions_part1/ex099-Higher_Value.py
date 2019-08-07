from time import sleep


def maior(* numeros):
    print('-' * 40)
    print('Analisando os valores passados.')
    for num in numeros:
        print(num, end=' ', flush=True)
        sleep(0.5)
    maior_num = 0 if (len(numeros) == 0) else max(numeros)

    print(f'Foram digitados {len(numeros)} valores.')
    print(f'O maior valor foi {maior_num}.')


maior(1, 6, 2, 8, 1, 9, 10, 90, 0, 2)  # Has 10 numbers. High is 90
maior(8, 3, 2)  # Has 3 numbers. High is 8
maior(3, 5)  # Has 2 numers. High is 5
maior()
maior(7)
maior(7, 7, 7, 7, 7)
