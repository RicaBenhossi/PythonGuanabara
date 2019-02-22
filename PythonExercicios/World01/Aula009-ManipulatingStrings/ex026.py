frase = str(input('Digite uma frase\n').strip())
print('A letra \'A\' aparece {} vez(es).'.format(frase.lower().count('a')))
print('A letra \'A\' aparece pela primeira vez na posição {}.'.format(frase.lower().find('a') + 1))
print('A letra \'A\' aparece pela útima vez na posição {}.'.format(frase.lower().rfind('a') + 1))
