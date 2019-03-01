tabuada = int(input('De qual número deseja saber a tabuada? '))
for x in range(1, 11):
    print('{} x {:2} = {:2}'.format(tabuada, x, (x * tabuada)))
