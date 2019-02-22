# I did this way
# from calendar import isleap
# ano = int(input('Digite um ano: '))
# if (isleap(ano)):
#     print('O ano de {} é bissexto!'.format(ano))
# else:
#     print('O ano de {} NÃO É bissexto.'.format(ano))

# Teacher did with math
from datetime import date
ano = (input('Digite o ano(enter para o ano atual): '))
if (ano == ''):
    ano = date.today().year
ano = int(ano)
if ((ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0)):
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO.'.format(ano))
