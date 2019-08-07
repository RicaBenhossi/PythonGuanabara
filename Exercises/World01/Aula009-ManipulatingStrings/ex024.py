cidade = str(input('Digite o nome da cidade\n').strip())
print('A cidade digitada começa com SANTO? -> {}'.format('santo' in cidade.lower()[:5]))
