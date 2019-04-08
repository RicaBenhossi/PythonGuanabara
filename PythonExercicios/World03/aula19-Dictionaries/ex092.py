from datetime import date

trabalhador = dict()

trabalhador['nome'] = str(input('Nome: '))
trabalhador['idade'] = date.today().year - int(input('ano de nascimento: '))
trabalhador['ctps'] = int(input('Número da CTPS [0 = Não possui]: '))
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Qual o ano da sua primeira contratação? '))
    trabalhador['salário'] = float(input('Qual o salário? '))
    trabalhador['aposentadoria'] = trabalhador['contratação'] + 35

for k, v in trabalhador.items():
    print(f'{k} tem valor {v}')
