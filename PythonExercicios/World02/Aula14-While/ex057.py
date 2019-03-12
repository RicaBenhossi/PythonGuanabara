sexo = str(input('Digite o sexo [F/M]: ')).upper().strip()[0]
while sexo not in 'MF':
    print('Sexo informado inválido. Digite novamente.')
print('O sexo digitado foi {}'.format('Feminino' if sexo in 'Ff' else 'Masculino'))
