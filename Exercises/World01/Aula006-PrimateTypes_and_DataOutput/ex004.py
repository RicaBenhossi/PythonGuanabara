coisa = input('Digite algo: ')
print('foi inserido um dado do tipo {}'.format(type(coisa)))
print('É alpha?                 {}'.format(coisa.isalpha()))
print('É numérico?              {}'.format(coisa.isnumeric()))
print('É alphanumérico?         {}'.format(coisa.isalnum()))
print('É uppercase?             {}'.format(coisa.isupper()))
print('É lowercase?             {}'.format(coisa.islower()))
print('É ASCII?                 {}'.format(coisa.isascii()))
print('É espaço em branco?      {}'.format(coisa.isspace()))
print('Está capitallizado?      {}'.format(coisa.istitle()))
print('É palavra Reservada?     {}'.format(coisa.isidentifier()))
