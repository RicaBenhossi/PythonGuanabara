# NOTE Possible structure of try
"""
try:
    # Validation you want to run
except:
    # Command to run if it doesn't pass the validation. Except could have a type error
else:
    # If succeeded, execute this
finally:
    # This commands will be executed after Try finishes. Will be executed anyway.
"""
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except:
    print('Erro!')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre...')


# NOTE You can capture the error of the command
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print('Erro encontrado.')
    print(f'Tipo: {erro.__class__}')
    print(f'Causa: {erro.__cause__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre...')

# NOTE We can have an exception specifically for a error type
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemosum problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir por Zero.')
except KeyboardInterrupt:
    print('Operador encerrou o sistema.')
except Exception as erro:
    print(f'Erro encontrado. Tipo: {error.__cause__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre...')
