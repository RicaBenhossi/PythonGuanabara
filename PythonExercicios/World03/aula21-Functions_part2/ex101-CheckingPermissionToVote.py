from datetime import date


def PodeVotar(nascimento):
    '''
    This function returns if the citizen is allowed to vote or not.

    Arguments: nascimento as the year the citizen borns
    Returns: String
    '''

    if ((date.today().year - nascimento) >= 18) and ((date.today().year - nascimento) < 65):
        return 'OBRIGATÓRIO'
    elif ((date.today().year - nascimento) >= 16) and ((date.today().year - nascimento >= 65)):
        return 'OPCIONONAL'
    else:
        return 'NEGADO'


nascimento = int(input('Informe o ano de seu nascimento: '))
print(f'Você possui {date.today().year - nascimento} anos e seu voto é {PodeVotar(nascimento)}.')
