cont = 1
while cont <= 10:  # thuis condition must be TRUE to continue.
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')

# If you need to run an iterator infinitevely, just put TRUE in the while condition

cont = 1
while True:
    print(cont, '-> ', end='')
    cont += 1
    if cont == 10:
        break  # This command stop the while Otherwise, it will run forever.
print('Acabou')

# This has a logical error
n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
# Variable s plus the flag value 999, which is wrong
print(f'A Soma vale {s}')  # This is a new wai to format print. WAY BETTER

# The right way is like this

n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break  # when we type the flag value, the iteration is interruptede and the instructions bellow aren't executed
    s += n
print(f'A Soma vale {s}')  # This is a new wai to format print. WAY BETTER

nome = 'José'
idade = 33
salário = 987.3
print(f'O {nome:=^20} tem {idade:->5} anos e ganha R${salário:.2f}')
