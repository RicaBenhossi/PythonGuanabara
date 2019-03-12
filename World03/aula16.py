lanche = 'haburguer'
print(lanche)
lanche = 'suco'
print(lanche)
# This is a Tuple.
lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[2])
print(lanche[1:3])
print(lanche[:3])
print(lanche[2:])
print(lanche[-1])
print(lanche[-3:])
# This command results an error because tuples are IMAUTABLE
# lanche[1] = 'Rerigerante'

# This is a way to iterate the tuple.
# In this case we can not show the index
for comida in lanche:
    print(f'Eu comi {comida}')
print('comi muito!')

# This is another way to iterate the tuple, but using the index
for x in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[x]} na posição {x}')
print('Comi Pra caramba!')

# This is another way to iterate a tuple by the index... Better

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi feito um pigodero!')

# We can sort it but it doesn't change the tuple
print(sorted(lanche))
print(lanche)

a = (2, 5, 4)
b = (5, 8, 1, 2)
# We can concatenate tuples
c = b + a
print(c)

# This command shows how many times the value shows in the tuple.
print(c.count(5))  # There is 2
print(c.count(4))  # There is 1
print(c.count(9))  # There is 0 (None)

# INDEX shows the index that the value is located
print(c.index(2))  # The first appearence of 2 is 4
print(c.index(8))  # Shows 1

# in a tuple we can have a lot of var types.
pessoa = ('Lola', 12, 'Catioro', 0.23)
print(pessoa)

# You can't change a tuple but you can delete it.
del(pessoa)
print(pessoa)
