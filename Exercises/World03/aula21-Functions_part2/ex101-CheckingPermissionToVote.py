# from datetime import date


def PodeVotar(nascimento):
    '''
    This function returns if the citizen is allowed to vote or not.

    Arguments: nascimento as the year the citizen borns
    Returns: String
    '''

    # We can use import insde a function which saves memory because will be used only in the function.
    from datetime import date

    # if ((date.today().year - nascimento) >= 18) and ((date.today().year - nascimento) < 65):
    #     return 'OBRIGATÓRIO'
    # elif ((date.today().year - nascimento) >= 16) and ((date.today().year - nascimento >= 65)):
    #     return 'OPCIONONAL'
    # else:
    #     return 'NEGADO'

    idade = (date.today().year - nascimento)
    if 18 <= idade < 65:
        return f'Você possui {idade} anos e seu voto é OBRIGATÓRIO.'
    elif (16 <= idade < 18) or (idade >= 65):
        return f'Você possui {idade} anos e seu voto é OPCIONONAL.'
    else:
        return f'Você possui {idade} anos e seu voto é NEGADO.'


nascimento = int(input('Informe o ano de seu nascimento: '))
# print(f'Você possui {date.today().year - nascimento} anos e seu voto é {PodeVotar(nascimento)}.') My way
print(PodeVotar(nascimento))
