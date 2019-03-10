multiplic = 0
while True:
    multiplic = int(input('Qual tabuada deseja visualizar? [Digite um valor negativo para sair] '))
    if multiplic < 0:
        break
    for x in range(1, 11):
        print(f'{multiplic:>3} X {x:>2} = {(multiplic * 3):>3}')
print('Finalizado!')
