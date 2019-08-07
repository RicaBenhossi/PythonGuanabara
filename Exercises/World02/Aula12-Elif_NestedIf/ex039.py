from datetime import date
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
if ((date.today().year - ano_nascimento) == 18):
    print('Está na hora de fazer o seu alistamento militar! Sorry')
elif ((date.today().year - ano_nascimento) < 18):
    print('Falta(m) {} ano(s) para você se alistar no serviço militar.'.format(18 - (date.today().year - ano_nascimento)))
else:
    print('Você já passou {} ano(s) do alistamento militar.'.format((date.today().year - ano_nascimento) - 18))
