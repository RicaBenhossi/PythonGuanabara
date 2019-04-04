num = [2, 5, 9, 1, 9, 3, 6, 2, 7, 0, 4]
print(num)
num[2] = 3
print(num)

# Add value
# APPEND insert a new item in the end.
num.append(7)
print('Append\n', num)
# INSERT can uses an index to determine where to add the value.
num.insert(2, 0)
print('Insert\n', num)

# SORT
num.sort()
print('Sort\n', num)
# Sort decrescent
num.sort(reverse=True)
print('sort(reverse=True)\n', num)
print(f'len \n', len(num))

# To reverse the order of a list
num.reverse()
print('reverse\n', num)

# Removing
# POP uses an index as parameter
num.pop()
print('pop()\n', num)
num.pop(2)
print('pop(2)\n', num)
# REMOVE uses the content as parameter
# to remove you may first check if the value exists
if 8 in num:
    num.remove(8)
    print('remove(8)\n', num)
else:
    print('Valor não está na lista.')
num.remove(2)
print('remove(2)\n', num)
# DEL works like pop
del num[6]
print('del num[6]\n', num)

valores = list((9, 5, 4))
# or you can do this way
# valores = []  # Also works with function LIST() -> valores = list() creates an empty list
# valores.append(9)
# valores.append(5)
# valores.append(4)
print(valores)

for v in valores:
    print(f'{v}...', end=' ')
print('Fim da lista')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}...')
print('fim da lista')

# You can make an nput inside the list
valores = list()

for x in range(0, 5):
    valores.append(int(input('Digite um número: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}...')
print('fim da lista')

a = [2, 3, 4, 7]
b = a  # This attribution crates a "mirror"
print(f'lista A {a}')
print(f'Lista B {b}')

b[2] = 80  # When you do this, it changes the original list too, in this case list a

print(f'lista A {a}')
print(f'Lista B {b}')

b = a[:]  # When you do this way, you copy all elements of list a into list b
b[2] = 100  # Now, you can change only list b

print(f'lista A {a}')
print(f'Lista B {b}')

c = a+b  # This makes a copy too.
c[3] = 1000
c[6] = 2999

print(f'lista A {a}')
print(f'Lista B {b}')
print(f'Lista C {c}')
