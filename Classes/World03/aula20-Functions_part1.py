# NOTE: Parameters in Python is passed by REFERENCES. So, the variable you pass as a parameter, will also change in mais code if changed in function.
def dobra(lst):
    for x in range(0, len(lst)):
        lst[x] *= 2


def soma2(* valores):
    print(sum(valores))

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}\n')


# NOTE: Packaging - Python allows you to pass a different quantity of parameters to functions using * on its'declaration. It'll generate a TUPLE.
def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros.')


# Main code
# a = 4
# b = 5
# s = a + b
# print(s)
soma(4, 5)
# a = 8
# b = 9
# s = a + b
# print(s)
soma(8, 9)
# a = 2
# b = 1
# s = a + b
# print(s)
soma(1, 2)

# NOTE: You can change the order of the parameters as long as you explicite it
soma(a=3, b=7)
soma(b=7, a=3)

# PACKAGING

# It causes an error becase SOMA has to receive only 2 parameters
# soma(3)
# soma(2, 5, 6)

contador(8, 0)
contador(2, 1, 7)
contador(4, 4, 7, 2)

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)


soma2(5, 2)
soma2(2, 9, 4)
