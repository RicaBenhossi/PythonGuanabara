media_idade = 0
nome_homem_mais_velho = ''
idade_homem_mais_velho = 0
qtd_mulheres_menor_20_anos = 0
for x in range(1, 5):
    print('{0} {1} PESSOA {0}'.format('=-' * 10, x))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [F/M]: '))
    media_idade += idade
    if (sexo.upper() == 'M'):
        if (nome_homem_mais_velho == ''):
            idade_homem_mais_velho = idade
            nome_homem_mais_velho = nome
        elif (idade_homem_mais_velho < idade):
            idade_homem_mais_velho = idade
            nome_homem_mais_velho = nome
    else:
        if (idade < 20):
            qtd_mulheres_menor_20_anos += 1
print('A média de idade do grupo é {}.'.format(media_idade / 5))
print('Neste grupo têm {} mulheres com menos de 20 anos.'.format(qtd_mulheres_menor_20_anos))
print('O homem mais velho se chama {} e tem {} anos.'.format(nome_homem_mais_velho, idade_homem_mais_velho))

