# NOTE: When help(your_method) it will show the docstring you put between """ """ right after the declaration of the method.
def docstring(a, b, c):
    '''
    *** Here you can put a manual to help others using this method
    param:
    @result result: none

    Author: Me.
    Date:
    '''
    pass


# NOTE: when you declare parameters as bellow, you set a default value to the parameter that will be assumed if no value was passed to it.
def optional_parameters(a=0, b=0, c=0):
    print(a+b+c)


# NOTE: variables in MAIN CODE are GLOBAL. Variables inside methods are LOCAL. If you want to use a global var inside method use command GLOBAl VAR
def variable_scope(a, b, c):
    global z
    z = 5  # This Z is the same Z as in maisn code. Change here to change there
    x = 8  # This X is a LOCAL VARIABLE. So we have 2 'X': One LOCAL (value = 8) and other GLOBAL (value = 3)
    print(f'Z inside = {z}')
    print(f'X inside = {x}')
    # We  didn't change Y var here. So there is no Y local.
    print(f'A = {a}')
    print(f'B = {b}')
    print(f'C = {c}')
    a *= 2  # Here, parameter A that is a copy of Z is doubled. It changes A (LOCAL) not Z (GLOBAL)
    b *= 2  # Here, parameter B that is a copy of X is doubled. It changes B (LOCAL) not X (GLOBAL)
    c *= 2  # Here, parameter C that is a copy of y is doubled. It changes C (LOCAL) not Y (GLOBAL)
    print(f'A * 2 = {a}')
    print(f'B * 2 = {b}')
    print(f'C * 2 = {c}')


# NOTE: Here the functio will return something to the point where it was called.
def returning_function(a, b, c):
    s = a + b + c
    print(f'\tMethod returning_function will return S({s}) which is the sum of A({a})+B({b})+C({c}).')
    return s


class ClassTeste():
    pass


# Main code
# NOTE: help() return to you the docstring and documentation of the method you passed. Type quit to exit.
# print('=' * 40)
# print('function help()')
# print(help(print))

# print('=' * 40)
# print('function help() on your own method with a docstring')
# print(help(docstring))

print('=' * 40)
print('Function with optional parameters')
optional_parameters(1, 2, 3)
optional_parameters(1, 3)
optional_parameters(1)
optional_parameters()

print('=' * 40)
print('Variable Scope')
z = 2
print(f'Z = {z}')
x = 3
print(f'X = {x}')
y = 4
print(f'\nY = {y}')
variable_scope(z, x, y)
# calling here variables a, b, c (from method) causes error.
print(f'Z after method = {z} -> Z has changed because we called it as GLOBAL inside method variable_scope')
print(f'X after method = {x} -> X has not been changed because X inside variable_scope is local.')
print(f'Y after method = {y} -> Y has not been changed because Y was not used inside variable_scope (neither GLOBAL nor LOCAL).')

print('=' * 40)
print('Function DocString')
docstring(2, 9, 9)

print('=' * 40)
print('Function with return')
r = (returning_function(4, 6, 8))
print(f'When calling function returning_function, r will receive value {r}.')

teste = "ok"
print(teste)
ClassTeste(True, 2, 2.0, 'Exact')
teste2 = True
