digitados = soma = 0
num = int(input('Digite o {} número: [999 para parar] '.format(digitados + 1)))
while num != 999:
    soma += num
    digitados += 1
    num = int(input('Digite o {} número: [999 para parar] '.format(digitados + 1)))
print('Foram digitados {} número(s) e Soma entre eles é {}.'.format(digitados, soma))

