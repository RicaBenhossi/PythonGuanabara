from random import randint

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Foram sorteados os números {n}')
print(f'O maior valor foi {sorted(n)[-1]}')
print(f'O menor valor foi {sorted(n)[0]}')

# Another way
print(f'O maior valor foi {max(n)}')
print(f'O menor valor foi {min(n)}')
