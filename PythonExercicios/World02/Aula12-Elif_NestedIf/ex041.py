from datetime import date

ano_nascimento = int(input('Informe o Ano de Nascimento do atleta:'))
if ((date.today().year - ano_nascimento) <= 9):
    print('Esse atleta pertence à categoria MIRIM.')
elif ((date.today().year - ano_nascimento) <= 14):
    print('Esse atleta pertece à categoria INFANTIL.')
elif ((date.today().year - ano_nascimento) <= 19):
    print('Esse atleta pertce à categoria JUNIOR.')
elif ((date.today().year - ano_nascimento) <= 20):
    print('Esse atleta pertence à categoria SÊNIOR.')
else:
    print('Esse atleta pertence à categoria MASTER.')
